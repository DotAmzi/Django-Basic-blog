from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    name = "Camilo"
    languages = ['Python', 'PHP', 'Java', 'Ruby']

    context = {
        'name': name,
        'languages': languages
    }

    return render(request, 'blog/home.html', context)
