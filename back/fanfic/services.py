from .models import Tag

def all_tags_service():
   return Tag.objects.all()