from django import forms


class CursoForm(forms.Form):  # En este punto se crea nuestro formulario.
    nombre = forms.CharField()  # Es muy similar a la sintaxis de creación de los modelos.
    camada = forms.IntegerField()


#La busqueda se realizará por el nombre del curso
class BusquedaCursoForm(forms.Form):
    nombre = forms.CharField()
