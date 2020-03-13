from django.shortcuts import render
from .models import Scam

def post_list(request):
	post = Scam.objects.all()
	return render(request, 'blog/post_list.html', {'posts': post})