from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_404_NOT_FOUND, 
                                   HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_204_NO_CONTENT, 
                                   HTTP_403_FORBIDDEN, 
                                   HTTP_401_UNAUTHORIZED)
from rest_framework.generics import (CreateAPIView, 
                                     RetrieveUpdateAPIView, 
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )
from rest_framework.permissions import IsAdminUser

from ..models import About
from ..serializers import (AboutSerializer, 
                           FanficRoolSerializer, 
                           FaqSerializer, 
                           PrivatyPoliceSerializer)
from ..services import (all_fanfic_rools_service,
                        all_faq_service, 
                        all_privaty_police_service,
                        all_about_service)
from ..utils import CreateOnlyPermission, AdminPermission

# ! /about
# TODO: Create
# * private
class AboutListView(ListCreateAPIView):
   queryset = all_about_service()
   serializer_class = AboutSerializer
   permission_classes =  [IsAdminUser]
   
# ! /about:id
# TODO: Show, Update
# * public(show), private(update)
class AboutDetailView(RetrieveUpdateAPIView):
   queryset = all_about_service()
   serializer_class = AboutSerializer
   permission_classes =  [AdminPermission]

      
# ! /fanfic-rool
# TODO: Create
# * private
class FanficRoolListView(CreateAPIView):
   queryset = all_fanfic_rools_service()
   serializer_class = FanficRoolSerializer
   permission_classes =  [IsAdminUser]

# ! /fanfic-rool/:id
# TODO:  Show, Update
# * public(get) private(update)
class FanficRoolDetailView(RetrieveUpdateAPIView):
   queryset = all_fanfic_rools_service()
   serializer_class = FanficRoolSerializer
   permission_classes =  [AdminPermission]
   
# ! /faq
# TODO: Create
# * public(show) private(create) 
class FaqListCreateAPIView(ListCreateAPIView):
   queryset = all_faq_service()
   serializer_class = FaqSerializer
   permission_classes =  [IsAdminUser ]

# ! /faq/:id
# TODO:  Update, Delete, Get
# * private
class FaqDetailView(RetrieveUpdateDestroyAPIView):
   queryset = all_faq_service()
   serializer_class = FaqSerializer
   permission_classes =  [AdminPermission]
   
# ! /private-policy
# TODO: Create
# * private
class PrivatyPoliceListView(CreateAPIView):
   queryset = all_privaty_police_service()
   serializer_class = PrivatyPoliceSerializer
   permission_classes =  [IsAdminUser]

# ! /private-policy/:id
# TODO:  Show, Update
# * public(get) private(update)
class PrivatyPoliceDetailView(RetrieveUpdateAPIView):
   queryset = all_privaty_police_service()
   serializer_class = PrivatyPoliceSerializer
   permission_classes =  [AdminPermission]