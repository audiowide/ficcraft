from .models import Tag, Fandom, Character, Pairing

def all_tags_service():
   return Tag.objects.all()

def all_fandoms_service():
   return Fandom.objects.all()

def all_characters_service():
   return Character.objects.all()