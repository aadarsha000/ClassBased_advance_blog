from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    Gender_Choice = (
        ("Male","male"),
        ("Female","Female"),
        ("Others","Others"),
    )
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=Gender_Choice, null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='images/%y/%m/%d', default="default.jpg", null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"