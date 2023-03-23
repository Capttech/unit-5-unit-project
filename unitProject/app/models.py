from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profile_pic = models.ImageField(
        null=True, blank=True, verbose_name="Profile Picture"
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
