from django.contrib.auth.models import AbstractUser
from django.db import models

class Area(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Administrador'),
        ('superempleado', 'SuperEmpleado'),
        ('empleado', 'Empleado'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)
    jefe = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='empleados'
    )

    def __str__(self):
        return f"{self.username} - {self.role}"
