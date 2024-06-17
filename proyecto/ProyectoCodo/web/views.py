from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
from .models import Alumno, Entrenador, Disciplina, Inscripciones
from django.views.generic.list import ListView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'web/index.html')

def user_logout(request):
    logout(request)

    return redirect('index')

class alumnos(ListView):
    model = Alumno
    context_object_name = 'alumnos'
    template_name = 'web/alumnos.html'
    ordering = ['apellido']


def alta_alumno(request):
    context={}

    if request.method == "GET":
        context ['form'] = AltaAlumno()
    else:
        form = AltaAlumno(request.POST)
        context ['form'] = form

        if form.is_valid():
            nuevo_alumno = Alumno(
                nombre = form.cleaned_data['nombre'],
                apellido = form.cleaned_data['apellido'],
                dni = form.cleaned_data['dni'],
            )

            nuevo_alumno.save()

            messages.success(request, '¡Listo! Tu inscripción como alumno fue procesada correctamente')
            
            return redirect('index')
    
    return render(request, 'web/alta_alumno.html', context)


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


def alta_entrenador(request):
    context = {}
    if request.method == "GET":
        form = AltaEntrenador()
    else:
        form = AltaEntrenador(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, '¡Listo! Tu inscripción como entrenador fue procesada correctamente')
            return redirect('index')
    
    context['form'] = form

    return render(request, 'web/alta_entrenador.html', context)


class disciplinas(ListView):
    model = Disciplina
    context_object_name = 'disciplinas'
    template_name = 'web/disciplinas.html'
    ordering = ['nombre', 'turno']


#@login_required
def inscripcion(request):
    context = {}
    if request.method == "GET":
        form = InscripcionForm()
    else:
        form = InscripcionForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, '¡Listo! Te inscribiste correctamente')
            return redirect('index')
    
    context['form'] = form

    return render(request, 'web/inscripcion.html', context)