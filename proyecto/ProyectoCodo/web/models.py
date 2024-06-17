from django.db import models
from ProyectoCodo import settings

class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='DNI')

    class Meta:
        abstract=True

class Alumno(Persona):

    user = models.OneToOneField(
	    settings.AUTH_USER_MODEL,
	    on_delete=models.CASCADE,
	    null=True,
	    blank=True
	    )

    def __str__(self):
        return f'{self.apellido} {self.nombre} DNI {self.dni}'

class Entrenador(Persona):
    email = models.EmailField(verbose_name='Email')

    user = models.OneToOneField(
	    settings.AUTH_USER_MODEL,
	    on_delete=models.CASCADE,
	    null=True,
	    blank=True
	)

    def __str__(self):
        return f'{self.apellido} {self.nombre}'

class Disciplina(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Disciplina o actividad')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')

    TURNOS=[
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche'),
    ]

    turno = models.CharField(max_length=10, choices=TURNOS, verbose_name='Turno')

    def __str__(self):
        return f'{self.nombre} turno {self.turno}'

class Inscripciones(models.Model):
    DISCIPLINAS=[
        ('voley', 'Voley'),
        ('basquet', 'Básquet'),
        ('natacion', 'Natación'),
    ]

    disciplina = models.CharField(max_length=50, choices=DISCIPLINAS, verbose_name='Disciplina')

    TURNOS=[
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche'),
    ]

    turno = models.CharField(max_length=10, choices=TURNOS, verbose_name='Turno')
    entrenador_id = models.ForeignKey(Entrenador, on_delete=models.CASCADE, null=True, blank=True)
    alumno_id = models.ManyToManyField(Alumno, null=True, blank=True)

    def __str__(self):
        return f'{self.disciplina} turno {self.turno} | Entrenador: {self.entrenador_id}'