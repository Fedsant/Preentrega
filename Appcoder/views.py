from django.http import HttpResponse
from django.shortcuts import render
from Appcoder.models import Curso


# Create your views here.

def crear_curso(request):
    curso = Curso(nombre="Python", camada=1234)
    curso.save()
    contexto = {"curso": curso}

    return render(request, 'index.html', contexto)



def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Fede"}
    return render(request, 'index.html', contexto)