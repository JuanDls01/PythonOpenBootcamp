# Siempre reciben por lo menos un parámetro las funciones de views, que es el request (petición)

from django.http import HttpResponse


def saludo(request):
    return HttpResponse('Hola Mundo')


def despedida(request):
    return HttpResponse('Hasta luego')
