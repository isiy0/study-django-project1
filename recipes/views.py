from django.shortcuts import render
from django.http import HttpResponse

def view_home(request):
    return HttpResponse("Hello World")

def view_contato(request):
    return HttpResponse("Página de contato")

def view_sobre(request):
    return HttpResponse("Página sobre")