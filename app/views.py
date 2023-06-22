from django.shortcuts import get_object_or_404, render, redirect
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . serializer import *
from .views import *
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.http import HttpResponse, JsonResponse
# from django.http.response import JsonResponse
# from django.http.response import Http404
# from rest_framework.response import Response

class LoginView(APIView):
    def get(self, request):
        output = [
        {"id": output.id,}
                  for output in Login.objects.all()]
        return Response("hello")
    
class MedicineView(APIView):
    
    def get(self, request):
        output = [
            {"id": output.id,
             "medicinename": output.medicinename,
             "medicineprice" : output.medicineprice,
             "medicinecategory" : output.medicinecategory,
             "medicineamount" : output.medicineamount,
             "medicineinputdate" : output.medicineinputdate,
             "medicineconfigurationdate" : output.medicineconfigurationdate,
             "medicineexpiredate" : output.medicineexpiredate}
            for output in Medicine.objects.all() ]
        return Response(output)
    
    def post(self, request):
        serializers = ReactSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
        else:
            return "data sizioni"

class MedicineInfo(APIView):
    def get(self, request,id):
        try:
            obj = Medicine.objects.get(id=id)
            
        except Medicine.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status.HTTP_404_NOT_FOUND)
        serializers = ReactSerializer(obj)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj = Medicine.objects.get(id=id)
            
        except Medicine.DoesNotExist:
            msg = {"msg" : "not found error"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializers = ReactSerializer(obj,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            obj = Medicine.objects.get(id=id)
            
        except Medicine.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msg":"deleted"}, status=status.HTTP_204_NO_CONTENT)
        
        
# Create your views here.
class CosmeticView(APIView):
    def get(self, request):
        output = [
            {"cosmeticname": output.cosmeticname,
             "cosmeticprice" : output.cosmeticprice,
             "cosmeticcategory" : output.cosmeticcategory,
             "cosmeticamount" : output.cosmeticamount,
             "cosmeticinputdate" : output.cosmeticinputdate,
             "cosmeticconfigurationdate" : output.cosmeticconfigurationdate,
             "cosmeticexpiredate" : output.cosmeticexpiredate}
            for output in Cosmetic.objects.all() ]
        return Response(output)
    
    def post(self, request):
        serializer = CosmeticSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return "data not found"

# Order your views here.
class OrderView(APIView):
    def get(self, request):
        output = [
            {"sendername": output.sendername,
             "senderaddress" : output.senderaddress,
             "dateposted" : output.dateposted,
             "timeposted" : output.timeposted,
             "statusorder" : output.statusorder}
            for output in Order.objects.all() ]
        return Response(output)
    
class AboutView(APIView):
    def get(self, request):
        output = [
            {
             "pharmacyvission" : output.pharmacyvission,
             "pharmacymission" : output.pharmacymission,
             "pharmacybackground" : output.pharmacybackground}
            for output in About.objects.all() ]
        return Response(output)
    
    def post(self, request):
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return "data not found"
    
class ContactView(APIView):
    def get(self, request):
        output = [
            {"pharmacyname": output.pharmacyname,
             "email" : output.email,
             "phonenumber" : output.phonenumber,
             "whatsappnumber" : output.whatsappnumber,
             "othernumber" : output.othernumber,
             "description" : output.description}
            for output in Contact.objects.all()]
        return Response(output)
    
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return "data not found"
    
class PharmacyView(APIView):
    def get(self, request):
        output = [
            {
             "pharmacyname": output.pharmacyname,
             "ownername" : output.ownername,
             "pharmacyaddress" : output.pharmacyaddress,
             "businesslicence" : output.businesslicence,
             "pharmacycontact" : output.pharmacycontact,
             "latitude" : output.latitude,
             "longitude" : output.longitude,
             "region" : output.region,
             }
            for output in Pharmacy.objects.all()]
        return Response(output)