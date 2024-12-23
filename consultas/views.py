from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta, Respuesta
from .forms import ConsultaForm, RespuestaForm
from django.contrib import messages

# Vista para enviar una nueva consulta
def enviar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)
            consulta.empleado = request.user
            consulta.save()
            messages.success(request, 'Consulta enviada correctamente.')
            return redirect('dashboard')
    else:
        form = ConsultaForm()

    return render(request, 'consultas/enviar_consulta.html', {'form': form})

# Vista para gestionar consultas y agregar respuestas (hilo de conversación)
def gestionar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    respuestas = consulta.hilo_respuestas.all().order_by('fecha_creacion')

    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.consulta = consulta
            respuesta.autor = request.user
            respuesta.save()
            messages.success(request, 'Respuesta añadida correctamente.')
            return redirect('gestionar_consulta', consulta_id=consulta.id)
    else:
        form = RespuestaForm()

    return render(request, 'consultas/gestionar_consulta.html', {
        'consulta': consulta,
        'respuestas': respuestas,
        'form': form
    })


# Vista para mostrar el dashboard con consultas enviadas y gestionarlas
def dashboard(request):
    consultas = Consulta.objects.filter(empleado=request.user)
    return render(request, 'dashboard.html', {'consultas': consultas})
