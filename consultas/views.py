from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Consulta
from .forms import ConsultaForm, RespuestaForm


# Vista para enviar consultas (Empleados)
@login_required
def enviar_consulta(request):
    if request.user.role != 'empleado':
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.empleado = request.user
            consulta.jefe = request.user.jefe
            consulta.save()
            return redirect('dashboard')
    else:
        form = ConsultaForm()

    return render(request, 'consultas/enviar_consulta.html', {'form': form})


# Vista para que SuperEmpleados respondan consultas
@login_required
def responder_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    
    if request.user != consulta.jefe:
        return redirect('dashboard')

    if request.method == 'POST':
        form = RespuestaForm(request.POST, instance=consulta)
        if form.is_valid():
            consulta.respondida = True
            form.save()
            return redirect('dashboard')
    else:
        form = RespuestaForm(instance=consulta)

    return render(request, 'consultas/responder_consulta.html', {'form': form, 'consulta': consulta})
