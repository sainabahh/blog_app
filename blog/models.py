# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def _str_(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def _str_(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User
    categories = models.ManyToManyField(Category)  # A post can have multiple categories
    tags = models.ManyToManyField(Tag)  # A post can have multiple tags
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically add timestamp

    def _str_(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # Link to Post
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f'Comment by {self.author} on {self.post}'
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
