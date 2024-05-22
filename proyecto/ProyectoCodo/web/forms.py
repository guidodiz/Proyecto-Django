from django import forms

class Inscripcion(forms.Form):

    nombre_apellido = forms.CharField(label='Nombre y apellido', required=True)
    dni = forms.IntegerField(label='DNI', required=True)
    email = forms.EmailField(label='Email', required=True)
    disciplina = forms.CharField(label='Disciplina/Deporte', required=True)
    dia = forms.CharField(label='Días a entrenar', required=True)
    horario = forms.CharField(label='Horario a entrenar', required=True)