from django.shortcuts import render
from . import models
from .serializers import UserSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


@csrf_exempt
def user_login(request):
    email =  request.POST['email']
    password =request.POST['password']
    try:
        user = models.User.objects.get(email=email,password=password)
    except models.User.DoesNotExist:
        user =None
    if user:
        return JsonResponse({"bool":True,"user_id":user.id})
    else:
        return JsonResponse({"bool":False})