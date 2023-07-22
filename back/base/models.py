from django.db import models

# Create your models here.
class About(models.Model):
   text = models.TextField(blank=True)
   
   def  __str__(self):
      return self.text
   
class News(models.Model):
   title = models.CharField(max_length=255, blank=True)
   description = models.TextField(max_length=5000, blank=True)
   
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   
   def  __str__(self):
      return self.title
   
class FanficRool(models.Model):
   text = models.TextField(max_length=255, blank=True)
   
   updated = models.DateTimeField(auto_now=True)
   
   def  __str__(self):
      return self.text
   
class Faq(models.Model):
   text = models.TextField(max_length=255, blank=True)
   
   def  __str__(self):
      return self.text
   
class PrivatyPolice(models.Model):
   text = models.TextField(max_length=255, blank=True)
   
   updated = models.DateTimeField(auto_now=True)
   
   def  __str__(self):
      return self.text