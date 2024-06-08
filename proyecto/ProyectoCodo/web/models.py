from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    dni = models.IntegerField(unique=True, verbose_name='DNI')

    class Meta:
        abstract=True

class Alumno(Persona):
    pass

class Entrenador(Persona):
    email = models.EmailField(verbose_name='Email')

class Disciplina(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Disciplina o actividad')
    descripcion = models.CharField(max_length=200, verbose_name='Descripción')

    TURNOS=[
        ('mañana', 'Mañana'),
        ('tarde', 'Tarde'),
        ('noche', 'Noche'),
    ]

    turno = models.CharField(max_length=10, choices=TURNOS, verbose_name='Turno')

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
    alumno_id = models.ManyToManyField(Alumno)