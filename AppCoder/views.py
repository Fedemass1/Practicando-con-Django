from django.shortcuts import render, redirect
from AppCoder.models import Curso


# Función para guardar información en la base de datos

def mostrar_cursos(request):
    cursos = Curso.objects.all()  # se conecta a la BD y me trae todos los cursos (objetos)
    contexto = {
        "cursos": cursos,
        "nombre": "Fede"
    }
    return render(request, "AppCoder/cursos.html", contexto)


def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)  # Cargo datos
    curso.save()  # Me guarda esta info en las tablas de la BD.

    return redirect("/app/cursos")


def show_html(request):
    cursos = Curso.objects.all()  # Traigo la info de la BD
    curso = Curso.objects.first()
    contexto = {"curso": curso, "cursos": cursos, "nombre": "Fede"}
    return render(request, 'index.html', contexto)
