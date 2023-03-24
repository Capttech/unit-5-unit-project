from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# ==========| MANAGER INFORMATION |==========#
class profileDatabase:
    userId = models.TextField()


# ==========| BUSINESS INFORMATION |==========#
class businessTemplateDatabase(models.Model):
    templateId = models.TextField()
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    type = models.TextField(max_length=255)
    missionStatement = models.TextField(max_length=1500)
    creationDate = models.DateField()
    profile = models.ForeignKey(
        profileDatabase, related_name="business", on_delete=models.CASCADE
    )


class businessContactDatabase(models.Model):
    email = models.TextField(max_length=255)
    phoneNumber = models.IntegerField()
    address = models.TextField()
    business = models.ForeignKey(
        businessTemplateDatabase, related_name="contact", on_delete=models.CASCADE
    )


class businessImagesDatabase(models.Model):
    image = models.ImageField()
    business = models.ForeignKey(
        businessTemplateDatabase, related_name="contact", on_delete=models.CASCADE
    )


# ==========| GENERATED WEBSITES |==========#
class generatedWebsites(models.Model):
    id = models.TextField()
    templateId = models.TextField()
    profile = models.ForeignKey(
        profileDatabase, related_name="websites", on_delete=models.CASCADE
    )
