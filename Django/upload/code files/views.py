from django.shortcuts import render,redirect,reverse
from .models import Movie
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views import View
from django.contrib.auth.decorators import login_required	
# Create your views here.
def movies_list(request):
	movies=Movie.objects.all()
	return render(request,"movies/movie_list.html",{"movies":movies});

def movies_detail(request,name):
	movie=Movie.objects.filter(name=name)
	print(movie)
	return render(request,"movies/movie_detail.html",{"movie":movie});
