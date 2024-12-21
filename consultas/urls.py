from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_consulta, name='enviar_consulta'),
    path('responder/<int:consulta_id>/', views.responder_consulta, name='responder_consulta'),
]
