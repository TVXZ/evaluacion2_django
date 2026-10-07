from django.shortcuts import render, redirect
from .models import Estudiante
from .forms import EstudianteForm

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