from .models import Tag, Fandom, Character, Pairing, Work

def all_tags_service():
   return Tag.objects.all()

def all_fandoms_service():
   return Fandom.objects.all()

def all_characters_service():
   return Character.objects.all()

def all_pairings_service():
   return Pairing.objects.all()

def all_works_service():
   return Pairing.objects.all()