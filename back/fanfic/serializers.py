from rest_framework.serializers import ModelSerializer
from .models import Tag, Fandom, Character, Pairing, Work, WorkComment, Chapter, ChapterComment
from user.serializers import UserSerializer

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
      fields = ('id', 'characters')
      
class CreatePairingSerializer(ModelSerializer):
   class Meta:
      model = Pairing
      fields = ('id', 'characters')
      
# Work
class WorkSerializer(ModelSerializer):
   tags = TagSerializer(many=True)
   user = UserSerializer(many=False)
   
   class Meta:
      model = Work
      fields = ('id', 
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
      
class ChapterSerializer(ModelSerializer):
   class Meta:
      model = Chapter
      fields =  ('id', '   ', 'title', 'pre_text', 'text', 'after_text', 'public', 'created', 'updated')

class WorkCommentSerializer(ModelSerializer):
   class Meta:
      model = WorkComment
      fields = ('id', 'user', 'work', 'body', 'created', 'updated')
      
class ChapterCommentSerializer(ModelSerializer):
   class Meta:
      model = ChapterComment
      field = ('id', 'user', 'chapter', 'body', 'created', 'updated')