from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Movie, Genre

# Create your views here.

def index(request):
    return render(request, 'views/index.html')

def catalog(request):
    movies = Movie.objects.all()
    #titles = ', '.join([m.title for m in movies])
    #return HttpResponse(titles)
    return render(request, 'views/catalogtest.html', { 'title': 'FROM BACKEND', 'movies': movies })

def test(request):
    return HttpResponse("This is a test page!")

def develop(request):
    return HttpResponse("<h1>Liz<h1>")
