from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from .models import Profile, Collection

class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = ('username', 'email', 'password', 'is_superuser')

class ProfileSerializer(ModelSerializer):
   user =  UserSerializer(many=False)
   
   class Meta:
      model = Profile
      fields = ('id', 'user', 'image', 'backImage', 'about', 'lowers', 'bookmarks', 'coins', 'updated', 'created')
      
class CollectionSerializer(ModelSerializer):
   user =  UserSerializer(many=False)
   
   class Meta:
      model = Collection
      fields = ('id', 'user', 'title', 'works')