from django.shortcuts import render
from ChartJs import models
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
# Create your views here.


class HomeView(View):
    def get(self, request,*args,**kwargs):
        return render(request,'charts.html',{})

def get_data(request, *args , **kwargs):
    data = {
        "Energy":150,
        "Runtime":150,
        "Power":60,
        }
    return JsonResponse(data) # http response in the form of json 

class ChartData(APIView):
   
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        labels=["Energy","Power","RunTime"]
        default_item=[60,80,50]
        data = {
        "labels":labels,
        "default":default_item,
        }
        return Response(data)