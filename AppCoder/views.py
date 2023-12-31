from django.http import HttpResponse
from django.shortcuts import render
from .models import Curso

def curso(req, nombre , camada):
    
    curso = Curso(nombre = nombre ,camada = camada)
    curso.save()
    
    return HttpResponse(f"""      
    <p>Curso: {curso.nombre} - Camada : {curso.camada}. Creada Con Exito!<p>
    """)

def listar_cursos(req):
    
    lista = Curso.objects.all()
    return render(req, "lista_cursos.html", {"lista_cursos":lista})