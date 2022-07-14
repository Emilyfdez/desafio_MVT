from django import http
from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from AppFamilia.models import Familia

# Create your views here.

def inicioApp(request):

    return render(request, 'AppFamilia/inicioApp.html')

def PersonaUno(self):    
    madre = Familia(nombre = "Katherine", apellido= "Márquez", edad = 41, fecha_nacimiento = "1980-12-23", profesion = "Azafata")


    madre.save()
    

    texto = f"Se creó al familiar: {madre.nombre} {madre.apellido}, de edad {madre.edad}, y fecha de nacimiento: {madre.fecha_nacimiento}"


    return HttpResponse(texto)

def PersonaDos(self):

    hermana = Familia(nombre = "Angela", apellido= "Fernández", edad = 17, fecha_nacimiento = "2005-05-21", profesion = "Estudiante")
    
    hermana.save()

    texto = f"Se creó al familiar: {hermana.nombre} {hermana.apellido}, de edad {hermana.edad}, y fecha de nacimiento: {hermana.fecha_nacimiento}"

    return HttpResponse(texto)


def PersonaTres(self):

    abuelo = Familia(nombre = "Tomás", apellido= "Márquez", edad = 62, fecha_nacimiento = "1960-05-18", profesion = "Jubilado")

    abuelo.save()

    texto = f"Se creó al familiar: {abuelo.nombre} {abuelo.apellido}, de edad {abuelo.edad}, y fecha de nacimiento: {abuelo.fecha_nacimiento}"

    return HttpResponse(texto)