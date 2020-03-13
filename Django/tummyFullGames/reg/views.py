from django.shortcuts import render, redirect
from .models import tribute
from .forms import PostForm

def post_list(request):
	post = tribute.objects.all()
	return render(request, 'reg/list.html', {'posts': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save()
			return redirect('post_list')
	else:
		form = PostForm()
	return render(request, 'reg/home.html', {'form': form})

def dist1(request):
	post = tribute.objects.filter(district=1)
	return render(request, 'reg/dist1.html', {'posts': post})

def dist2(request):
	post = tribute.objects.filter(district=2)
	return render(request, 'reg/dist2.html', {'posts': post})

def dist3(request):
	post = tribute.objects.filter(district=3)
	return render(request, 'reg/dist3.html', {'posts': post})

def dist4(request):
	post = tribute.objects.filter(district=4)
	return render(request, 'reg/dist4.html', {'posts': post})