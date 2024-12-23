from django.db import models
from usuarios.models import User

class Consulta(models.Model):
    empleado = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consultas')
    jefe = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respuestas')
    asunto = models.CharField(max_length=100)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    respondida = models.BooleanField(default=False)

class Respuesta(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE, related_name='hilo_respuestas')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    mensaje = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Respuesta de {self.autor.username} - {self.consulta.asunto}"
