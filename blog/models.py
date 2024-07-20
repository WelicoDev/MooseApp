from django.db import models
from users.models import CustomUser
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250 , blank=True , null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='post-img')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    content = models.TextField()
    description = models.TextField()
    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}  {self.user.username}"

class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    subject = models.CharField(max_length=250)
    message = models.TextField(null=True , blank=True)

    is_solved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class Information(models.Model):
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200)
    location = models.TextField(max_length=5000, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

    is_public = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message