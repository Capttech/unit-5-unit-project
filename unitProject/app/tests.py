from django.test import TestCase
from app import manager as system

# Create your tests here.
class TestCreation(TestCase):
    def testCreate(self):
        business = system.createBusinessTemplate(
            "LSC", "This is a test company", "NonProfit", "We build new so you do not"
        )

        self.assertEquals(business.name, "LSC")
        self.assertEquals(business.description, "This is a test company")
        self.assertEquals(business.type, "NonProfit")
        self.assertEquals(business.missionStatement, "We build new so you do not")

    def testCreateSecond(self):
        business = system.createBusinessTemplate(
            "LSC", "This is a test company", "NonProfit", "We build new so you do not"
        )
        businessContact = system.createBusinessContact(
            "joe@gmail.com", "(662) 417-5820", "10-15 Sinner St", business
        )

        self.assertEquals(business.name, "LSC")
        self.assertEquals(business.description, "This is a test company")
        self.assertEquals(business.type, "NonProfit")
        self.assertEquals(business.missionStatement, "We build new so you do not")

        self.assertEquals(businessContact.email, "joe@gmail.com")
        self.assertEquals(businessContact.phoneNumber, "(662) 417-5820")
        self.assertEquals(businessContact.address, "10-15 Sinner St")

        self.assertEquals(businessContact.business.name, "LSC")

    def testCreateWebsite(self):
        business = system.createBusinessTemplate(
            "LSC", "This is a test company", "NonProfit", "We build new so you do not"
        )

        website = system.generateWebsite(business.templateId)

        self.assertEquals(website.templateId, business.templateId)
