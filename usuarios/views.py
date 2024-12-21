from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User


# Vista para iniciar sesión
def custom_login(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')

    return render(request, 'usuarios/login.html')


# Vista para cerrar sesión
def custom_logout(request):
    logout(request)
    return redirect('login')


# Vista del dashboard para SuperEmpleados y Empleados
@login_required
def dashboard(request):
    user = request.user
    if user.role == 'superempleado':
        empleados = User.objects.filter(jefe=user)
        return render(request, 'usuarios/dashboard_super.html', {'empleados': empleados})
    
    elif user.role == 'empleado':
        return render(request, 'usuarios/dashboard_empleado.html', {'user': user})
    
    return redirect('admin:index')  # Si es admin, redirige al admin
