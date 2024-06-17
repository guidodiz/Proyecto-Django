from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from web.models import Alumno, Entrenador
from .serializers import AlumnoSerializer, EntrenadorSerializer


class AlumnosViewSet(viewsets.ModelViewSet):
	queryset = Alumno.objects.all()
	serializer_class = AlumnoSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EntrenadoresViewSet(viewsets.ModelViewSet):
	queryset = Entrenador.objects.all()
	serializer_class = EntrenadorSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]