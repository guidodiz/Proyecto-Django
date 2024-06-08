from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('alumnos', views.alumnos.as_view(), name='alumnos'),
    path('alta_alumno', views.alta_alumno, name='alta_alumno'),
    path('entrenador/<str:nombre>', views.entrenador, name='entrenador'),
    path('alta_entrenador', views.alta_entrenador, name='alta_entrenador'),
    path('disciplinas', views.disciplinas.as_view(), name='disciplinas'),
    path('inscripcion', views.inscripcion, name='inscripcion')
] 