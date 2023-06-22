from django.db import models
from django.db import connections

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=50)

class Medicine(models.Model):
    # id = models.CharField(max_length=100)
    medicinename = models.CharField(max_length=200)
    medicineprice = models.CharField(max_length=200)
    medicinecategory = models.CharField(max_length=200)
    medicineamount = models.CharField(max_length=200)
    medicineinputdate = models.CharField(max_length=200)
    medicineconfigurationdate = models.CharField(max_length=200)
    medicineexpiredate = models.CharField(max_length=200)
    medicinelogo = models.CharField(max_length=200)
    
    def __str__(self):
        return self().medicine_model
    
    
    
class Cosmetic(models.Model):
    cosmeticname = models.CharField(max_length=100)
    cosmeticprice = models.CharField(max_length=200)
    cosmeticcategory = models.CharField(max_length=200)
    cosmeticamount = models.CharField(max_length=200)
    cosmeticinputdate = models.CharField(max_length=200)
    cosmeticconfigurationdate = models.CharField(max_length=200)
    cosmeticexpiredate = models.CharField(max_length=200)
    cosmeticlogo = models.CharField(max_length=200)
    
    
class Order(models.Model):
    sendername = models.CharField(max_length=100)
    senderaddress = models.CharField(max_length=200)
    dateposted = models.CharField(max_length=200)
    timeposted = models.CharField(max_length=200)
    statusorder = models.CharField(max_length=200)
    
class About(models.Model):
    pharmacymission = models.CharField(max_length=200)
    pharmacyvission = models.CharField(max_length=200)
    pharmacybackground = models.CharField(max_length=200)
    
    
class Contact(models.Model):
    pharmacyname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phonenumber = models.CharField(max_length=200)
    whatsappnumber = models.CharField(max_length=200)
    othernumber = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
class Pharmacy(models.Model):
    pharmacyname = models.CharField(max_length=200)
    ownername = models.CharField(max_length=200)
    pharmacyaddress = models.CharField(max_length=200)
    businesslicence = models.CharField(max_length=200)
    pharmacycontact = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    