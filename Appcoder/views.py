from django.http import HttpResponse
from django.shortcuts import render
from Appcoder.models import Curso


# Create your views here.

def crear_curso(request):
    curso = Curso(nombre="Python", camada=1234)
    curso.save()

    return HttpResponse(f"su curso es {curso.nombre} y la cada es {curso.camada}")
