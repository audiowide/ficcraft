from django.contrib import admin
from .models import (Tag, 
                     Fandom, 
                     Character,
                     Pairing, 
                     Work, 
                     Chapter, 
                     WorkComment, 
                     ChapterComment)

admin.site.register(Tag)
admin.site.register(Fandom)
admin.site.register(Character)
admin.site.register(Pairing)
admin.site.register(WorkComment)
admin.site.register(ChapterComment)
admin.site.register(Chapter)
admin.site.register(Work)
