from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('HOME 1')


def sobre(request):
    return HttpResponse("Sobre")


def contato(request):
    return HttpResponse("contato")
