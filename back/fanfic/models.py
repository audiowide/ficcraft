from django.db import models
from django.contrib.auth.models import User
   
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
   description = models.TextField(max_length=500, blank=True)
   
   def __str__(self):
      return self.name
   
class Character(models.Model):
   name = models.CharField(max_length=200)
   fandom = models.ForeignKey(Fandom, on_delete=models.CASCADE)
   description = models.TextField(max_length=500, blank=True)
   
   def __str__(self):
      return self.name
   
class Pairing(models.Model):
   characters = models.ManyToManyField(Character, default=[])
   
   def __str__(self):
      character_names = self.characters.values_list('name', flat=True)
      return '/'.join(character_names)
   
   def pairing(self):
      character_names = self.characters.values_list('name', flat=True)
      return '/'.join(character_names)
   
class Work(models.Model):
   AUTHORTYPE = (
      ('Work of my authorship', 'Work of my authorship'),
      ('Translation', 'Translation'),
   )
   
   FANFICTYPE = (
      ('Original', 'Original'),
      ('Fandom fan fiction', 'Fandom fan fiction'),
   )
   
   RAITING = (
      ('Whole audience', 'Whole audience'),
      ('Teenagers', 'Teenagers'),
      ('Mature', 'Mature'),
      ('Adults Only', 'Adults Only'),
   )
   
   ORIENTATION = (
      ('Gen', 'Gen'),
      ('Female/Male', 'Female/Male'),
      ('Male/Male', 'Male/Male'),
      ('Female/Female','Female/Female'),
      ('Multi', 'Multi'),
      ('Other', 'Other'),
   )
   TYPE = (
      ('In progress', 'In progress'),
      ('Finished', 'Finished'),
      ('Frozen', 'Frozen'),
   )
   
   title = models.CharField(max_length=300)
   slug = models.CharField(max_length=300, unique=True)
   image = models.ImageField(upload_to='images/', default='book.jpeg', blank=True)
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   workType = models.CharField(max_length=100, choices=AUTHORTYPE, default='Work of my authorship')
   fanfic_type = models.CharField(max_length=100, choices=FANFICTYPE,  default='Original')
   
   fandoms = models.ManyToManyField(Fandom, blank=True)
   characters = models.ManyToManyField(Character, blank=True)
   pairings = models.ManyToManyField(Pairing, blank=True)
   
   raiting = models.CharField(max_length=100, choices=RAITING)
   orientation = models.CharField(max_length=100, choices=ORIENTATION)
   
   tags = models.ManyToManyField(Tag, default=[])
   
   description = models.TextField(blank=True, max_length=1000)
   notes = models.TextField(blank=True, max_length=1000)
   
   progressType = models.CharField(max_length=20, choices=TYPE, default='In progress')
   public = models.BooleanField(default=False)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.title
   
class Chapter(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   work = models.ForeignKey(Work, on_delete=models.CASCADE, default='')
   title = models.CharField(max_length=300)
   
   pre_text = models.TextField(max_length=1000)
   text = models.TextField()
   after_text = models.TextField(max_length=1000)
   
   public = models.BooleanField(default=False)
   place = models.IntegerField(default=0)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.title
   
class WorkComment(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   work = models.ForeignKey(Work, on_delete=models.CASCADE)
   
   parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE) 
   body = models.TextField(blank=True, max_length=1000)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.user.username
   
class ChapterComment(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   chapter = models.ForeignKey(WorkComment, on_delete=models.CASCADE)
   body = models.TextField(blank=True, max_length=1000)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.user.username
   