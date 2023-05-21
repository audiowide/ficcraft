from django.contrib.auth.models import User

def authenticate(email, password):
   try:
      user = User.objects.get(email=email)
      
      if user.password == password:
         return user
      return None
   except:
      return None