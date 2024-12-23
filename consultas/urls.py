from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_consulta, name='enviar_consulta'),
    path('gestionar/<int:consulta_id>/', views.gestionar_consulta, name='gestionar_consulta'),
]
