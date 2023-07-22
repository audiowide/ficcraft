from django.db import models

from fanfic.models import Work, Chapter, Fandom, Pairing, Character
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   
   avatar = models.ImageField(upload_to='profile/avatars', default='', blank=True)
   background = models.FileField(upload_to='profile/background-image/',  default='', blank=True)
      
   about = models.TextField(blank=True)
   
   lowers = models.ManyToManyField(Work, default=[])
   bookmarks = models.ManyToManyField(Chapter, default=[])
   
   fandom_bookmarks = models.ManyToManyField(Fandom, default=[])
   pairing_bookmarks = models.ManyToManyField(Pairing, default=[])
   character_bookmarks = models.ManyToManyField(Character, default=[])
   
   # chats = models.ManyToManyField('Chat', default=[])
   # users = models.ManyToManyField(User, default=[])
   
   coins = models.IntegerField(default=0)
   
   updated = models.DateTimeField(auto_now_add=True)
   created = models.DateTimeField(auto_now=True)
   
   def __str__(self):
      return self.user.username
   
# TODO: Work Collections
class Collection(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   title =  models.CharField(max_length=250)
   works = models.ManyToManyField(Work, default=[])
   public = models.BooleanField(default=False)
   
   def __str__(self):
      return self.title
   
# TODO: Chat with messages
# class ChatMessage(models.Model):
#    message = models.TextField(max_length=1000)
   
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
   
#    def __str__(self):
#       return self.message
   
# class Chat(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    user2 = models.ForeignKey(User, on_delete=models.SET_NULL)
   
#    messages = models.ManyToManyField(ChatMessage, default=[])
   
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
   
#    def __str__(self):
#       return "{} - {}".format(self.user.username, self.user.username2)