from django import forms
from .models import Estudiante, Asignatura

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['rut', 'nombre', 'apellido', 'email', 'carrera']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: 12345678-9'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ejemplo@correo.com'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['codigo', 'nombre', 'creditos', 'estudiante']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej: INF-101'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
            'estudiante': forms.Select(attrs={'class': 'form-select'}),
        }