from django.contrib import admin
from django.urls import path
from universidad.views import lista_estudiantes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lista_estudiantes, name='lista_estudiantes'),
]