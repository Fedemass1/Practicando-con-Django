from django.urls import path
from AppCoder.views import crear_curso, show_html, mostrar_cursos

# Solo tendré las URL de mi aplicación AppCoder

urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('show/', show_html),
    path('cursos/', mostrar_cursos),


]
