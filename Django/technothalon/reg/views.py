from django.shortcuts import render, redirect
from .models import team
from .forms import PostForm


def post_list(request):
    post = team.objects.all()
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


def zeus(request):
    post = team.objects.filter(uni='Zeus University')
    return render(request, 'reg/zeus.html', {'posts': post})


def apollo(request):
    post = team.objects.filter(uni='Apollo University')
    return render(request, 'reg/apollo.html', {'posts': post})


def nike(request):
    post = team.objects.filter(uni='Nike University')
    return render(request, 'reg/nike.html', {'posts': post})


def hermes(request):
    post = team.objects.filter(uni='Hermes University')
    return render(request, 'reg/hermes.html', {'posts': post})
