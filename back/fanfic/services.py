from .models import (Tag, 
                     Fandom, 
                     Character, 
                     Pairing, 
                     Work, 
                     WorkComment, 
                     ChapterComment)

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

def all_work_comments_service():
   return WorkComment.objects.all()

def all_chapter_comments_service():
   return ChapterComment.objects.all()