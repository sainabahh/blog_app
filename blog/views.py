# Create your views here.

# blog/views.py
from .models import Post  # Assuming you have a Post model


from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def post_list(request):
    posts = list(Post.objects.values())  # Get all posts as a list of dictionaries
    return JsonResponse(posts, safe=False)  # Return posts as JSON

def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
        return JsonResponse(post)
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)





from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer  # Updated import

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer 


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'success': f'Account created for {user.username}!'}, status=status.HTTP_201_CREATED)
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ObtainAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
