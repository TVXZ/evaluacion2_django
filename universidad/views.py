from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Asignatura
from .forms import EstudianteForm, AsignaturaForm

def lista_estudiantes(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
        
    estudiantes = Estudiante.objects.all()
    return render(request, 'universidad/lista_estudiantes.html', {
        'estudiantes': estudiantes,
        'form': form
    })

def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'universidad/editar_estudiante.html', {'form': form, 'estudiante': estudiante})

def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    estudiante.delete()
    return redirect('lista_estudiantes')

def lista_asignaturas(request):
    if request.method == 'POST':
        form = AsignaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asignaturas')
    else:
        form = AsignaturaForm()

    asignaturas = Asignatura.objects.select_related('estudiante').all()
    return render(request, 'universidad/lista_asignaturas.html', {
        'asignaturas': asignaturas,
        'form': form
    })