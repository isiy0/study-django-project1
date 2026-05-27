from django.shortcuts import render
from django.http import HttpResponse


def view_home(request):
    return render(request, "recipes/home.html")


def view_contato(request):
    return render(request, "contato.html")


def view_sobre(request):
    return render(request, "sobre.html")
