from django.contrib import admin
from .models import Estudiante, Asignatura

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'email', 'carrera')
    search_fields = ('rut', 'nombre', 'apellido')

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creditos', 'estudiante')
    search_fields = ('codigo', 'nombre')
    list_filter = ('creditos',)