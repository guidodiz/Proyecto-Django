from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect

def index(request):
    return render(request, 'web/index.html')

def entrenador(request, nombre):
    context={
        'nombre': nombre
    }

    return render(request, 'web/entrenador.html', context)

def alumnos(request, nombre):
    context={
        'nombre': nombre
    }

    return render(request, 'web/alumnos.html', context)

def disciplinas(request):
    context={
        'disciplina1':{'nombre':'Voley', 'dias': 'Lunes, Martes y Viernes', 'horario': '17 hs'},
        'disciplina2':{'nombre':'Voley', 'dias': 'Martes y Jueves', 'horario': '18 hs'},
        'disciplina3':{'nombre':'Natación', 'dias': 'Lunes, Martes y Viernes', 'horario': '17 hs'},
        'disciplina4':{'nombre':'Natación', 'dias': 'Martes y Jueves', 'horario': '18 hs'},
        'disciplina5':{'nombre':'Básquet', 'dias': 'Lunes, Martes y Viernes', 'horario': '17 hs'},
        'disciplina6':{'nombre':'Básquet', 'dias': 'Martes y Jueves', 'horario': '18 hs'},
        }

    return render(request, 'web/disciplinas.html', {'disciplinas':context})

def inscripciones(request):
    context={}

    if request.method == "GET":
        context ['form'] = Inscripcion()
    else:
        context ['form'] = Inscripcion(request.POST)
        return redirect('index')
    
    return render(request, 'web/inscripciones.html', context)