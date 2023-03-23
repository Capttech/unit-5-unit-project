from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(
        max_length=20,
    )
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.CharField(max_length=1000)


class SignUp(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    repeated_password = models.CharField(max_length=20)


class Company(models.Model):
    name = models.CharField(max_length=20)


from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profile_pic = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
