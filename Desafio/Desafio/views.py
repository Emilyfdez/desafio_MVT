from django.http import HttpResponse


def inicio(self):

    texto = "BIENVENIDO"

    return HttpResponse(texto)