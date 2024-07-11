from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Добро пожаловать на главную страницу.")
# Create your views here.
