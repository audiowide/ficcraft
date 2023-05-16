from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   
   image = models.ImageField(upload_to='profile/avatars/', blank=True)
   backImage = models.ImageField(upload_to='profile/background-image/', blank=True)
   
   about = models.TextField(blank=True)
   
   # lowers = models.ManyToManyField()
   # bookmarks = models.ManyToManyField()
   # chats = models.ManyToManyField()
   # subcribed = models.ManyToManyField()
   # watched = models.ManyToManyField()
   
   coins = models.IntegerField(default=0)
   
   updated_at = models.DateTimeField(auto_now_add=True)
   created_at = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.user.username
   
class Collection(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   title =  models.CharField(max_length=250)
   # works = models.ManyToManyField(Work, default=[])
   
   def __str__(self):
      return self.user.username
   
class Tag(models.Model):
   name = models.CharField(max_length=100)
   description = models.TextField(max_length=500, blank=True)
   
   def __str__(self):
      return self.name
   
class Fandom(models.Model):
   TYPES = (
      ('Books & Novels', 'Books & Novels'),
      ('Anime & Manga', 'Anime & Manga'),
      ('Real People', 'Real People'),
      ('Music & Musicals', 'Music & Musicals'),
      ('Video Games', 'Video Games'),
      ('Cartoons & Comics', 'Cartoons & Comics'),
      ('Movies', 'Movies'),
      ('TV Shows', 'TV Shows'),
      ('Other', 'Other'),
   )
   name = models.CharField(max_length=500)
   type = models.CharField(max_length=100, blank=True, choices=TYPES)
   description = models.TextField(max_length=500)
   
   def __str__(self):
      return self.name
   
class Cahacter(models.Model):
   name = models.CharField(max_length=200)
   fandom = models.ForeignKey(Fandom, on_delete=models.CASCADE)
   description = models.TextField(max_length=500, blank=True)
   
   def __str__(self):
      return name
   
class Pairing(models.Model):
   characters = models.ManyToManyField(Cahacter, default=[])
   
   def __str__(self):
      return self.id
   
class Work(models.Model):
   AUTHORTYPE = (
      ('Work of my authorship', 'Work of my authorship'),
      ('Translation', 'Translation'),
   )
   
   title = models.CharField(max_length=300)
   slug = models.CharField(max_length=300, unique=True)
   authorType = models.CharField(max_length=100, 
                                 choices=AUTHORTYPE, 
                                 default='Work of my authorship')
   