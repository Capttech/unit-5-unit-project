from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# =====| User info |=========#
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profile_pic = models.ImageField(
        upload_to="profiles/",
        verbose_name="Profile Picture",
        null=True,
        blank=True,
        default="/profiles/profile_pic_green.png",
    )
    date_created = models.DateTimeField(auto_now_add=True)
    business = models.ForeignKey(
        "businessTemplateDatabase", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


# ==========| BUSINESS INFORMATION |==========#
class businessTemplateDatabase(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    type = models.TextField(max_length=255)
    missionStatement = models.TextField(max_length=1500)
    creationDate = models.DateField()
    profile = models.ManyToManyField(Profile, related_name="business")


class businessContactInfoDatabase(models.Model):
    email = models.TextField(max_length=255)
    phoneNumber = models.IntegerField()
    address = models.TextField()
    business = models.ForeignKey(
        businessTemplateDatabase, related_name="contact", on_delete=models.CASCADE
    )


# ==========| GENERATED WEBSITES |==========#
class generatedWebsites(models.Model):
    id = models.TextField()
    profile = models.ForeignKey(
        Profile, related_name="websites", on_delete=models.CASCADE
    )
