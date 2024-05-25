from django import forms
from django.core.exceptions import ValidationError

class Inscripcion(forms.Form):

    nombre = forms.CharField(label='Nombre', required=True)
    apellido = forms.CharField(label='Apellido', required=True)
    dni = forms.IntegerField(label='DNI', required=True)
    email = forms.EmailField(label='Email', required=True)

    DISCIPLINAS=[
        ('Elegir', 'Elegir'),
        ('voley', 'Voley'),
        ('basquet', 'Básquet'),
        ('natacion', 'Natación'),
    ]

    disciplina = forms.ChoiceField(label='Disciplina', choices=DISCIPLINAS, required=True)

    TURNOS=[
        ('Elegir', 'Elegir'),
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche'),
    ]

    turno = forms.ChoiceField(label='Turno', choices=TURNOS, required=True)


    def clean_nombre(self):
        if not self.cleaned_data["nombre"].isalpha():
            raise ValidationError('El nombre solo puede estar compuesto por letras')
        return self.cleaned_data["nombre"]

    def clean_apellido(self):        
        if not self.cleaned_data["apellido"].isalpha():
            raise ValidationError('El apellido solo puede estar compuesto por letras')
        return self.cleaned_data["apellido"]

    def clean_dni(self):
        if self.cleaned_data['dni'] <= 999999:
            raise ValidationError('El número de DNI debe tener al menos 7 dígitos')
        return self.cleaned_data['dni']

    def clean_disciplina(self):
        if self.cleaned_data['disciplina'] == 'Elegir':
            raise ValidationError('Debe seleccionar una disciplina disponible')
        return self.cleaned_data['disciplina']

    def clean_turno(self):
        if self.cleaned_data['turno'] == 'Elegir':
            raise ValidationError('Debe seleccionar un turno disponible')
        return self.cleaned_data['turno']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        apellido = cleaned_data.get('apellido')

        if nombre and apellido:
            if nombre.lower() == apellido.lower():
                raise ValidationError('El nombre y el apellido no pueden ser iguales')
        return cleaned_data