from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_401_UNAUTHORIZED,
                                   HTTP_403_FORBIDDEN,
                                   HTTP_400_BAD_REQUEST,
                                   HTTP_201_CREATED
                                   )
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken

from django.contrib.auth.hashers import make_password

from ..validation import validate_email, validate_username
from ..utils import authenticate

from ..models import Profile

   
# ! /sign-up
# TODO: Sign Up
# * public
@api_view(['POST'])
def sign_up_view(request):
   username = validate_username(request.data['username'])
   email = validate_email(request.data['email'])
   password = request.data['password']
   password_confirmation = request.data['password_confirmation']
      
   if password_confirmation != password:
      return Response({'message': 'Password1 does not match password'},
                       status=HTTP_400_BAD_REQUEST)
      
   user = User.objects.create(
      username=username, 
      email=email, 
      password=make_password(password))
   
   refresh  = RefreshToken.for_user(user)
   
   refresh_token = str(refresh)
   token = str(refresh.access_token)
   
   return Response({
      'refresh_token': refresh_token,
      'token': token,
      }, status=HTTP_201_CREATED)
   
# ! /sign-in
# TODO: Sign In
# * public
@api_view(['POST'])
def sign_in_view(request):
   email = request.data.get('email')
   password = request.data.get('password')
   user  = authenticate(email, password)
   
   if user is not None:
      login(request, user)
      
      refresh = RefreshToken.for_user(user)
      
      refresh_token = str(refresh)
      access_token = str(refresh.access_token)
   
      return Response({
         'refresh_token': refresh_token,
         'access_token': access_token
         }, status=HTTP_200_OK)
   else:
      return Response({'message': 'user not found'}, 
         status=HTTP_401_UNAUTHORIZED)
      
# ! /sign-out
# TODO: Sign Out
# * private
@api_view(['POST'])
def sign_out_view(request):
   authorization_header = request.headers.get('Authorization')
   if authorization_header and authorization_header.startswith('Bearer '):
      access_token = authorization_header.split(' ')[1]
   
      try:
         # token = RefreshToken(access_token)
         # token.revoke()
         
         return Response({'message': 'logout successful'}, 
                   status=HTTP_200_OK)
      except:
         return Response({'message': 'Token incorrect'}, 
                       status=HTTP_403_FORBIDDEN)  
   else:
       return Response({'message': 'Token not found'}, 
                       status=HTTP_401_UNAUTHORIZED)     
  