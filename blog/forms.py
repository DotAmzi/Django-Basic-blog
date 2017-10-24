from django.forms import ModelForm

from blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'name', 'content', 'status']
