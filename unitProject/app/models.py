from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# =====| User info |=========#
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    profile_pic = models.ImageField(
        upload_to="profiles/",
        verbose_name="Profile Picture",
        null=True,
        blank=True,
        default="/profiles/profile_pic_green.png",
    )
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


# ==========| BUSINESS INFORMATION |==========#
class businessTemplateDatabase(models.Model):
    templateId = models.TextField()
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    type = models.TextField(max_length=255)
    missionStatement = models.TextField(max_length=1500)
    profile = models.ForeignKey(
        Profile, related_name="business", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class businessContactInfoDatabase(models.Model):
    email = models.TextField(max_length=255)
    phoneNumber = models.IntegerField(verbose_name="phone number")
    address = models.TextField()
    business = models.ForeignKey(
        businessTemplateDatabase, related_name="contact", on_delete=models.CASCADE
    )


# ==========| GENERATED WEBSITES |==========#
class generatedWebsites(models.Model):
    webId = models.TextField()
    templateId = models.TextField()
    profile = models.ForeignKey(
        Profile, related_name="websites", on_delete=models.CASCADE
    )


# ====| what bryan is working on below |=========

# ==========| TEMPLATE |==========#
class Template(models.Model):
    name = models.CharField(max_length=255)
    html = models.TextField()
    css = models.TextField()

    def __str__(self):
        return self.name


# ==========| SUBMISSION |==========#
from django.db import models
from django.contrib.auth.models import User


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    template = models.CharField(max_length=100)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # New field
    profile = models.ForeignKey("app.Profile", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.template}"


# # ====| end of bryan's work |=========
