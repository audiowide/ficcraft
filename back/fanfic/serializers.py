from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Tag, Fandom, Character, Pairing, Work, WorkComment, Chapter, ChapterComment
from user.serializers import UserSerializer
from .services import (all_characters_service, 
                       all_fandoms_service, 
                       all_pairings_service, 
                       all_tags_service)


# Tag
class TagSerializer(ModelSerializer):
   class  Meta:
      model = Tag
      fields = ('id' ,'name', 'description', )
      
# Fandom
class FandomSerializer(ModelSerializer):
   class Meta:
      model = Fandom
      fields = ('id', 'name', 'type', 'description')
    
# Character   
class CharacterSerializer(ModelSerializer):
   fandom = FandomSerializer()
   
   class Meta:
      model = Character
      fields = ('id', 'name', 'fandom','description')
      
class CreateCharacterSerializer(ModelSerializer):
   class Meta:
      model = Character
      fields = ('id', 'name', 'fandom','description')
      
# Pairing  
class PairingCharacterSerializer(ModelSerializer):
   class Meta:
      model = Character
      fields = ('id', 'name')
      
class PairingSerializer(ModelSerializer):
   characters = PairingCharacterSerializer(many=True)
   
   class Meta:
      model = Pairing
      fields = ('id', 'pairing', 'characters')
      
   def pairing(self, instance):
        return instance.get_character_names()
      
class CreatePairingSerializer(ModelSerializer):
   class Meta:
      model = Pairing
      fields = ('id', 'characters')
      
# Work
class WorkSerializer(ModelSerializer):
   user = UserSerializer(many=False)
   
   fandoms = FandomSerializer(many=True)
   characters = CharacterSerializer(many=True)
   pairings = PairingSerializer(many=True)
   tags = TagSerializer(many=True)
   
   class Meta:
      model = Work
      fields = ('id', 'title', 'slug', 'image', 'user', 'workType', 'fanfic_type', 'fandoms', 'characters',
                  'pairings', 'raiting', 'orientation', 'tags', 'description', 'notes', 'progressType', 'public',
                  'created', 'updated')
      
# Work
class CreateWorkSerializer(ModelSerializer):
   class Meta:
      model = Work
      fields = ('id', 'title', 'image', 'workType', 'fanfic_type', 'fandoms', 'characters',
                  'pairings', 'raiting', 'orientation', 'tags', 'description', 'notes', 'progressType', 'public',
                  'created', 'updated')
      
class ChapterSerializer(ModelSerializer):
   class Meta:
      model = Chapter
      fields =  ('id', 'title', 
                 'user', 'work', 
                 'pre_text', 'text', 'after_text','place', 
                 'public', 'created', 'updated')

class WorkCommentSerializer(ModelSerializer):
   class Meta:
      model = WorkComment
      fields = ('after_textid', 
                'user', 'work', 
                'body', 
                'created', 'updated')
      
class ChapterCommentSerializer(ModelSerializer):
   class Meta:
      model = ChapterComment
      field = ('id', 
               'user', 'chapter', 
               'body', 
               'created', 'updated')