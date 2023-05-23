from rest_framework.serializers import ModelSerializer
from .models import Tag, Fandom, Character, Pairing, Work, WorkComment, Chapter, ChapterComment


class TagSerializer(ModelSerializer):
   class  Meta:
      model = Tag
      fields = ('id' ,'name', 'description', )
      
class FandomSerializer(ModelSerializer):
   class Meta:
      model = Fandom
      fields = ('id', 'name', 'type', 'description')
      
class CharacterSerializer(ModelSerializer):
   class Meta:
      model = Character
      fields = ('id', 'name', 'description', 'fandom')
      
class PairingSerializer(ModelSerializer):
   class Meta:
      model = Pairing
      fields = ('id', 'characters')
      
class WorkSerializer(ModelSerializer):
   tags = TagSerializer(many=True)

   class Meta:
      model = Work
      field = ('id', 
                  'title', 
                  'slug', 
                  'image', 
                  'user', 
                  'workType', 
                  'fanfic_type', 
                  'fandom', 
                  'characters', 
                  'pairings',
                  'raiting', 
                  'orientation',
                  'tags', 'description', 'notes', 'progressType', 'public', 'created', 'updated')