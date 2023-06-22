from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from . models import *
from rest_framework.views import APIView
from rest_framework.response import Response

UserModel = get_user_model()

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    ##
    def check_user(self, clean_data):
        user = authenticate(username=clean_data['email'], password=clean_data['password'])
        if not user:
            raise ValidationError('user not found')
        return user
    
    
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = [
            'id',
            'medicinename',
            'medicineprice',
            'medicinelogo',
            'medicinecategory',
            'medicineamount',
            'medicineinputdate',
            'medicineconfigurationdate',
            'medicineexpiredate'
        ]
        
        

        
        
class CosmeticSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Cosmetic
        fields = [
            'cosmeticname',
            'cosmeticprice',
            'cosmeticlogo',
            'cosmeticcategory',
            'cosmeticamount',
            'cosmeticinputdate',
            'cosmeticconfigurationdate',
            'cosmeticexpiredate'
        ]
        
class OrderSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Order
        fields = [
            'sendername',
            'senderaddress',
            'dateposted',
            'timeposted',
            'statusorder'
        ]
class AboutSerializer(serializers.ModelSerializer): 
    class Meta:
        model = About
        fields = [
            'pharmacyvission',
            'pharmacymission',
            'pharmacybackground',
        
        ]  
        
class ContactSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Contact
        fields = [
            'pharmacyname',
            'email',
            'phonenumber',
            'whatsappnumber',
            'othernumber',
            'description',
        
        ]   
        
        
class PharmacySerializer(serializers.ModelSerializer): 
      class Meta:
        model = Pharmacy
        fields = [
            'pharmacyname',
            'ownername',
            'pharmacyaddress',
            'businesslicence',
            'pharmacycontact',
            'latitude',
            'longitude',
            'region'
        
        ]   