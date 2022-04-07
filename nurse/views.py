from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
# Create your views here.
class Test(APIView):
    def get(self,request):
        response={}
        hospital=Hospital.objects.all()
        for h in hospital:
            response[h.id]={
                "id":h.id,
                "name":h.name,
                "image":h.image.url if h.image else None
            }
        return Response(response.values())

class AWSTest(APIView):
    def get(self,request):
        
        return Response({"message":"without models class is working"})