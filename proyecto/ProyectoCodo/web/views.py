from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from .models import Alumno, Entrenador, Disciplina, Inscripcion

def index(request):
    return render(request, 'web/index.html')

def entrenador(request, nombre):
    context={
        'nombre': nombre,
        'cursos': {
            '1':{'disciplina': 'Natación', 'turno': 'Noche'},
            '2':{'disciplina': 'Básquet', 'turno': 'Mañana'},
            '3':{'disciplina': 'Voley', 'turno': 'Tarde'},
            '4':{'disciplina': 'Básquet', 'turno': 'Mañana'}
        }
    }

    return render(request, 'web/entrenador.html', context)

def alumnos(request, nombre):
    context={
        'nombre': nombre
    }

    return render(request, 'web/alumnos.html', context)

def disciplinas(request):

    disciplinas = Disciplina.objects.all().order_by('nombre')
    
    context={
        'disciplinas': disciplinas
    }
    
    return render(request, 'web/disciplinas.html', context)

def inscripciones(request):
    context={}

    if request.method == "GET":
        context ['form'] = Inscripcion()
    else:
        form = Inscripcion(request.POST)
        context ['form'] = form

        if form.is_valid():
            messages.success(request, '¡Listo! Tu inscripción fue procesada correctamente')
            return redirect('index')
    
    return render(request, 'web/inscripciones.html', context)