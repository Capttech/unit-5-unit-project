import random
from .models import *

# ==========| GENERATE USER ID |==========#
def generateUserId():
    list1 = [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
    ]
    return f"{random.choice(list1)}{random.choice(list1)}{random.choice(list1)}{random.choice(list1)}{random.choice(list1)}"


# ==========| CREATE BUSINESS TEMPLATE |==========#
def createBusinessTemplate(name, description, type, mission):
    createdWebId = generateUserId()
    business = businessTemplateDatabase(
        name=name,
        description=description,
        type=type,
        missionStatement=mission,
        templateId=createdWebId,
    )
    business.save()
    return business


# ==========| CREATE BUSINESS TEMPLATE CONTACT |==========#
def createBusinessContact(email, phone, address, business):
    businessContact = businessContactInfoDatabase(
        email=email, phoneNumber=phone, address=address, business=business
    )
    businessContact.save()
    return businessContact


# ==========| CREATE WEBSITE TEMPLATE |==========#
def generateWebsite(templateId, profile):
    createdWebId = generateUserId()
    website = generatedWebsites(
        webId=createdWebId, profile=profile, templateId=templateId
    )
    website.save()
    return website


# ==========| GET WEBSITE |==========#
def getWebsiteData(websiteId):
    pass
