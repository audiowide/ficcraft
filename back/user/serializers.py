from rest_framework.serializers import ModelSerializer

from django.contrib.auth.models import User
from .models import Profile, Collection
# from fanfic.serializers import WorkSerializer


class UserSerializer(ModelSerializer):
   class Meta:
      model = User
      fields = ('username', 'email', 'password', 'is_superuser')

class ProfileSerializer(ModelSerializer):
   user =  UserSerializer(many=False)
   
   # lowers = WorkSerializer(many=True)
   # bookmarks = WorkSerializer(many=True)
   
   class Meta:
      model = Profile
      fields = ('id', 
                'user', 
                'avatar', 
                'background', 
                'about', 
                'lowers', 
                'bookmarks', 
                'coins', 
                'updated', 'created')
      
class CollectionSerializer(ModelSerializer):
   user =  UserSerializer(many=False)
   
   class Meta:
      model = Collection
      fields = ('id', 'user', 'title', 'works', 'public')