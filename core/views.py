from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello, World!');

def indexHome(request):
    return render(request, 'home.html', {"Usuario": "Dyego Wolf"})
