from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={'name': 'Leonardo'})


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={'name': 'Leonardo'})