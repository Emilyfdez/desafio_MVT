from django.contrib import admin
from django.urls import include,path
from .views import inicioApp, PersonaUno, PersonaDos, PersonaTres

urlpatterns = [
    path('', inicioApp),
    path('Personauno/', PersonaUno),
    path('Personados/', PersonaDos),
    path('Personatres/', PersonaTres),

]

