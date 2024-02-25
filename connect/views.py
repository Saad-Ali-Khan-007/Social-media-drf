from django.shortcuts import render
from . import models
from .serializers import UserSerializer,PostSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.


class UserList(generics.ListCreateAPIView):
    queryset = models.User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
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
        return JsonResponse({"bool":True,"user_id":user.id,"user_name":user.name})
    else:
        return JsonResponse({"bool":False})
    

class PostList(generics.ListCreateAPIView):
    queryset = models.Post.objects.all().order_by("-created")
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = PostSerializer

    