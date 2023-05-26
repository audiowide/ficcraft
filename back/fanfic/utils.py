from .models import Work
from random import randrange

def slug_generator(title):
   slug = '-'.join(title.lower().split(' '))
    
   work = Work.objects.filter(slug=slug)
   
   if (work.count() > 0):
      slug += str(randrange(10000))
      return slug 
   else:
      return slug 
    