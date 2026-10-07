from django.contrib import admin
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'email', 'carrera', 'fecha_ingreso')
    search_fields = ('rut', 'nombre', 'apellido', 'email')
    list_filter = ('carrera',)