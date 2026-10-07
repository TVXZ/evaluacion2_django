from django.db import models

class Estudiante(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"


class Asignatura(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    creditos = models.IntegerField(default=5)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name='asignaturas')

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"