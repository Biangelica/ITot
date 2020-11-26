from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return HttpResponse(request, "hello.html")

def sobre(request):
    return HttpResponse("<h1>Sobre nós</h1>")

def contato(request):
    return HttpResponse("<h1>Contato</h1>")