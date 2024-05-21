from django import forms

class Alquiler(forms.Form):

    nombre_apellido = forms.CharField(label='Nombre y apellido', required=True)
    email = forms.EmailField(label='Email', required=True)
    tituto = forms.CharField(label='Título del libro', required=True)
    autor = forms.CharField(label='Autor', required=True)
    año = forms.IntegerField(label='Año de publicación', required=True)