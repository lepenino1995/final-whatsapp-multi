from django.db import models
from usuarios.models import User

class Consulta(models.Model):
    empleado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultas')
    jefe = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respuestas')
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    respuesta = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    respondida = models.BooleanField(default=False)

    def __str__(self):
        return f"Consulta de {self.empleado.username} a {self.jefe.username}"
