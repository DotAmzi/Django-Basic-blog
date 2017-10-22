from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Category, Post

# Create your views here.

def home(request):

    name = "Camilo"
    # categories = ['PHP', 'Java', 'Ruby']
    # for category in categories:
    #     Category.objects.create(name=category)

    all_categories = Category.objects.all()
    category_python = Category.objects.get(name='Python')
    post = Post.objects.get(pk=1)

    # post = Post()
    # post.name = "My first very post"
    # post.content = "Content of my first post"
    # post.status = "Published"
    # post.category = category_python
    #
    # post.save()

    context = {
        'name': name,
        'categories': all_categories,
        'post': post,
    }

    return render(request, 'blog/home.html', context)
