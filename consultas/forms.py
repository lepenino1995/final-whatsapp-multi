from django import forms
from .models import Consulta, Respuesta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['asunto', 'mensaje']
        widgets = {
            'asunto': forms.TextInput(attrs={
                'class': 'w-full p-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Escribe el asunto aquí...'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'w-full p-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400',
                'rows': 6,
                'placeholder': 'Describe tu consulta detalladamente...'
            })
        }


class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['mensaje']
        widgets = {
            'mensaje': forms.Textarea(attrs={
                'class': 'w-full p-4 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400',
                'rows': 5,
                'placeholder': 'Escribe tu respuesta aquí...'
            })
        }

