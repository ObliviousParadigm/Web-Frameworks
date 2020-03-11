from django.shortcuts import render

posts = [
    {
        'name': 'Adarsh',
        'age': '20',
        'sex': 'male'
    },
    {
        'name': 'Mishu',
        'age': '20',
        'sex': 'female'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About Blog'})
