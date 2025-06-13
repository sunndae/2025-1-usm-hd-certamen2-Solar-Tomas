from django import forms 
from .models import Comuna

class ComunaForm(forms.ModelForm):
    class Meta:
        model = Comuna
        fields = ['nombre', 'poblacion', 'tasa_de_vulnerabilidad' ]