from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('asunto', 'empleado', 'jefe', 'respondida', 'fecha_creacion')
    list_filter = ('respondida', 'jefe')
    search_fields = ('asunto', 'empleado__username', 'jefe__username')
