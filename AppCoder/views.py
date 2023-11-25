from django.shortcuts import render, redirect
from AppCoder.models import Curso
from AppCoder.forms import CursoForm, BusquedaCursoForm


# Función para guardar información en la base de datos

def mostrar_cursos(request):
    cursos = Curso.objects.all()  # se conecta a la BD y me trae todos los cursos (objetos)
    contexto = {
        "cursos": cursos,
        "nombre": "Fede",
        "form": BusquedaCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", contexto)


def crear_curso(request):
    curso = Curso(nombre="Python", camada=47785)  # Cargo datos
    curso.save()  # Me guarda esta info en las tablas de la BD.

    return redirect("/app/cursos")


def crear_curso_form(request):

    curso_formulario = CursoForm
    contexto = {
        "form": curso_formulario,
        "nombre": "Fede"
    }

    if request.method == "POST":

        # Creando curso
        curso_formulario = CursoForm(request.POST)  # Recibo datos por request en la web y se los cargo

        # Valido el formulario
        if curso_formulario.is_valid():
            informacion = curso_formulario.cleaned_data  # Me trae los datos en el tipo correcto

            curso_crear = Curso(nombre=informacion["nombre"], camada=informacion["camada"])
            curso_crear.save()  # Guardo el curso en la BD
            return redirect("/app/cursos")

    return render(request, "AppCoder/crear_curso.html", contexto)

def busqueda_camada(request):
    nombre = request.GET["nombre"] #El request.GET es un diccionario
    cursos = Curso.objects.filter(nombre__icontains=nombre)  # Vamos a filtrar acorde al nombre que
    #contenga la BD. nombre__icontains es es de la BD, mientras que nombre es lo que ingreso el usuario.

    contexto = {

        "cursos": cursos,
        "nombre": "Fede",
        "form": BusquedaCursoForm(),
    }
    return render(request, "AppCoder/cursos.html", contexto)



def show_html(request):
    cursos = Curso.objects.all()  # Traigo la info de la BD
    curso = Curso.objects.first()
    contexto = {"curso": curso, "cursos": cursos, "nombre": "Fede"}
    return render(request, 'index.html', contexto)
