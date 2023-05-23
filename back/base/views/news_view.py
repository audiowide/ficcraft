from rest_framework.generics import ( ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from ..serializers import  NewsSerializer
from ..services import all_news_service
from ..utils import CreateOnlyPermission, AdminPermission

#! /news
# TODO: Create, Show All
#* private(create) 
class NewsListView(ListCreateAPIView):
   queryset = all_news_service()
   serializer_class = NewsSerializer
   permission_classes =  [AdminPermission]

#! /news/:id
# TODO:  Show, Update, Delete
#* private(update, delete) 
class NewsDetailView(RetrieveUpdateDestroyAPIView):
   queryset = all_news_service()
   serializer_class = NewsSerializer
   permission_classes =  [AdminPermission]
   