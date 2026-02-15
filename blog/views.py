from django.shortcuts import render
from .models import Post


posts = [
    {
        'author' : 'Titiksha Mishra',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'February 13, 2026'
    },
    {
        'author' : 'Tanvi Mishra',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'February 13, 2026'
    }
]

def home(request):
    context = {'posts' : Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})