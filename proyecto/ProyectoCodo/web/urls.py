from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('entrenador/<str:nombre>', views.entrenador, name='entrenador'),
    path('alumnos/<str:nombre>', views.alumnos, name='alumnos'),
    path('disciplinas', views.disciplinas, name='disciplinas'),
    path('inscripciones', views.inscripciones, name='inscripciones'),
] 