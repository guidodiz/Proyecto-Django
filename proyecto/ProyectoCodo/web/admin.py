from django.contrib import admin
from .models import Alumno, Entrenador, Disciplina, Inscripciones

admin.site.register(Alumno)
admin.site.register(Entrenador)
admin.site.register(Disciplina)
admin.site.register(Inscripciones)