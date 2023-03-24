from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# ==========| MANAGER INFORMATION |==========#
class managerDatabase:
    userId = models.TextField()


# ==========| BUSINESS INFORMATION |==========#
class businessTemplateDatabase(models.Model):
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=255)
    type = models.TextField(max_length=255)
    missionStatement = models.TextField(max_length=1500)
    creationDate = models.DateField()
    manager = models.ManyToManyField(managerDatabase, related_name="business")


class businessContactInfoDatabase(models.Model):
    email = models.TextField(max_length=255)
    phoneNumber = models.IntegerField()
    address = models.TextField()
    business = models.ForeignKey(
        businessDatabase, related_name="contact", on_delete=models.CASCADE
    )


# ==========| GENERATED WEBSITES |==========#
class generatedWebsites(models.Model):
    id = models.TextField()
    business = models.ForeignKey(
        businessDatabase, related_name="websites", on_delete=models.CASCADE
    )
