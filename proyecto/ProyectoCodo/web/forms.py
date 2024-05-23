from django import forms
from django.core.exceptions import ValidationError

class Inscripcion(forms.Form):

    nombre_apellido = forms.CharField(label='Nombre y apellido', required=True)
    dni = forms.IntegerField(label='DNI', required=True)
    email = forms.EmailField(label='Email', required=True)
    disciplina = forms.CharField(label='Disciplina/Deporte', required=True)
    dia = forms.CharField(label='Días a entrenar', required=True)
    horario = forms.CharField(label='Horario a entrenar', required=True)

    def clean_nombre_apellido(self):
        if not self.cleaned_data["nombre_apellido"].isalpha():
            raise ValidationError('El campo solo puede estar compuesto por letras')
        return self.cleaned_data["nombre_apellido"]

#Clean general
    #def clean(self):
        