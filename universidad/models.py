from django.db import models

class Estudiante(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    carrera = models.CharField(max_length=100)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.rut})"