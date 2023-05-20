from django.db import models

# Create your models here.
class About(models.Model):
   description = models.TextField(max_length='5000', blank=True)
   
class News(models.Model):
   title = models.CharField(max_length=255, blank=True)
   description = models.TextField(max_length=5000, blank=True)
   
   
   
class FanficRool(models.Model):
   text = models.TextField(max_length=255, blank=True)
   