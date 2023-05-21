from rest_framework.serializers import ModelSerializer
from .models import News, About, FanficRool, Faq, PrivatyPolice

class NewsSerializer(ModelSerializer):
   class Meta:
      model = News
      fields = '__all__'
      
class AboutSerializer(ModelSerializer):
   class Meta:
      model = About
      fields = '__all__'
      
class FanficRoolSerializer(ModelSerializer):
   class Meta:
      model = FanficRool
      fields = '__all__'
      
class FaqSerializer(ModelSerializer):
   class Meta:
      model = Faq
      fields = '__all__'

class PrivatyPoliceSerializer(ModelSerializer):
   class Meta:
      model = PrivatyPolice
      fields = '__all__'