from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)


class Category (models.Model):

    name = models.CharField(max_length=255)

    class Meta:

        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):

    category = models.ForeignKey(Category)
    name = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Draft')

    def __str__(self):
        return self.name
