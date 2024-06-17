from rest_framework import serializers
from web.models import Alumno, Entrenador

class AlumnoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Alumno
		fields = ['id', 'dni', 'apellido', 'nombre']

class EntrenadorSerializer(serializers.ModelSerializer):

	class Meta:
		model = Entrenador
		fields = ['id', 'dni', 'apellido', 'nombre']