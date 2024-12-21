from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['asunto', 'mensaje']


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['respuesta']
