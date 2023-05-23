from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.status import (HTTP_401_UNAUTHORIZED, 
                                   HTTP_403_FORBIDDEN)
from rest_framework.response import Response

from django.contrib.auth.models import User

# user authentication for sign in
def authenticate(email, password):
   try:
      user = User.objects.get(email=email)
      
      if user.password == password:
         return user
      return None
   except:
      return None
   
def auth_check(request):
   authorization_header = request.headers.get('Authorization')
   if authorization_header and authorization_header.startswith('Bearer '):
      token = authorization_header.split(' ')[1]
      
      try:
         payload = tokens.AccessToken(token, verify=False)
         user = User.objects.get(id = payload['user_id'])
      
         return token
      except:
         return Response("Token incorrect",
                      status=HTTP_403_FORBIDDEN)   
   else:
      return Response("Token not found",
                      status=HTTP_401_UNAUTHORIZED)