from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.hashers import make_password, check_password

from rest_framework.status import (HTTP_401_UNAUTHORIZED, 
                                   HTTP_403_FORBIDDEN)
from rest_framework.response import Response

from django.contrib.auth.models import User

# user authentication for sign in
def authenticate(email, password):
   try:
      user = User.objects.get(email=email)
      
      if check_password(password, user.password):
         return user
      return None
   except:
      return None
   
def auth_check(request):
   authorization_header = request.headers.get('Authorization')
   if authorization_header and authorization_header.startswith('Bearer '):
      token = authorization_header.split(' ')[1]
      
      try:
         payload = AccessToken(token, verify=False)
         id = payload['user_id']
         
         return ['success', id]
      except:
         return ['error', 'Token incorrect', 403]  
   else:
      return ['error', 'Token not found', 401]
   