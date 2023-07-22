from .models import News, FanficRool, Faq, PrivatyPolice, About

def all_news_service():
   return News.objects.all()

def all_fanfic_rools_service():
   return FanficRool.objects.all()

def all_faq_service():
   return Faq.objects.all()

def all_privaty_police_service():
   return PrivatyPolice.objects.all()

def all_about_service():
   return About.objects.all()