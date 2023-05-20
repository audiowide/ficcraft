from rest_framework.serializers import ModelSerializer
from .models import Tag, Fandom, Character, Pairing

class TagSerializer(ModelSerializer):
   class  Meta:
      model = Tag
      fields = ('id' ,'name', 'description', )