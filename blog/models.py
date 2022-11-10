from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# model for blog post category
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    


# model for the blog post
class Post(models.Model):
    STATUS_CHOICES = (
        ("DRAFT","DRAFT"),
        ("PUBLISHED", "PUBLISHED"),
    )
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to="images/blog/%Y/%m/%d", default="images/blog/default.jpg")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="DRAFT")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

