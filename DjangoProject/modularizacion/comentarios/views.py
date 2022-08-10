from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Comment


def test(request):
    return HttpResponse('Funciona Correctamente')


def create(request):
    # Forma 1:
    # comment = Comment(name='Juan', score=5, text='Este es un comentario')
    # comment.save()

    # Forma 2:
    comment = Comment.objects.create(
        name='Alex', text='Este es el segundo comentario')
    return HttpResponse('Comentario creado correctamente')


def delete(request):
    # Forma 1:
    # Primero necesitamos buscar el comentario
    # comment = Comment.objects.get(id=1)
    # Eliminamos el comentario encontrado:
    # comment.delete()

    # Forma 2:
    Comment.objects.filter(id=2).delete()
    return HttpResponse('Comentario eliminado correctamente')
