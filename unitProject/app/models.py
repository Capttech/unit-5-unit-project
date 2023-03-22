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
    email = models.EmailField()
    password = models.CharField(max_length=20)
    repeated_password = models.CharField(max_length=20)


class Company(models.Model):
    name = models.CharField(max_length=20)
