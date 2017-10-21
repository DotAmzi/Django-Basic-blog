from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category

# Create your views here.

def home(request):

    name = "Camilo"
    # categories = ['PHP', 'Java', 'Ruby']
    # for category in categories:
    #     Category.objects.create(name=category)

    all_categories = Category.objects.all()

    context = {
        'name': name,
        'categories': all_categories
    }

    return render(request, 'blog/home.html', context)
