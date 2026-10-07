from django.contrib import admin
from django.urls import path
from universidad import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('editar/<int:pk>/', views.editar_estudiante, name='editar_estudiante'),
    path('eliminar/<int:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),
    path('asignaturas/', views.lista_asignaturas, name='lista_asignaturas'),
]