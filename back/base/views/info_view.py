from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_404_NOT_FOUND, 
                                   HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_204_NO_CONTENT)
from rest_framework.generics import (CreateAPIView, 
                                     RetrieveUpdateAPIView, 
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )

from ..models import About
from ..serializers import (AboutSerializer, 
                           FanficRoolSerializer, 
                           FaqSerializer, 
                           PrivatyPoliceSerializer)
from ..services import (all_fanfic_rools_service,
                        all_faq_service, 
                        all_privaty_police_service)


# ! /about
# TODO: Create About
# * private(create, update, delete) 
@api_view(['POST'])
def aboutCreateView(request):
   about = About.objects.create(
      text=request.data['text'],
   )
   
   return Response(AboutSerializer(about, many=False).data, 
                   status=HTTP_201_CREATED)

# ! /about/:id
# TODO: Get and Update about
# * public(GET), private(PUT)
@api_view(['GET', 'PUT'])
def aboutDetailView(request, pk):   
   try:
      about = About.objects.get(id=pk)
      
      if request.method == 'GET':
         return Response(AboutSerializer(about, many=False).data, 
                         status=HTTP_200_OK)
      
      if request.method == 'PUT':
         if about.text != request.data['text']:
            about.text = request.data['text']
         else:
            return Response({'message': "Text doesn't changed"}, 
                            status=HTTP_204_NO_CONTENT)
            
         about.save()
         return Response(AboutSerializer(about, many=False).data, 
                         status=HTTP_201_CREATED)
   except:
      return Response({'message': 'About not found'}, 
                      status=HTTP_404_NOT_FOUND)
      
# ! /fanfic-rool
# TODO: Create
# * private
class FanficRoolListView(CreateAPIView):
   queryset = all_fanfic_rools_service()
   serializer_class = FanficRoolSerializer

# ! /fanfic-rool/:id
# TODO:  Show, Update
# * public(get) private(update)
class FanficRoolDetailView(RetrieveUpdateAPIView):
   queryset = all_fanfic_rools_service()
   serializer_class = FanficRoolSerializer
   
# ! /faq
# TODO: Create
# * public(show) private(create) 
class FaqListCreateAPIView(ListCreateAPIView):
   queryset = all_faq_service()
   serializer_class = FaqSerializer

# ! /faq/:id
# TODO:  Update, Delete, Get
# * private
class FaqDetailView(RetrieveUpdateDestroyAPIView):
   queryset = all_faq_service()
   serializer_class = FaqSerializer
   
# ! /private-policy
# TODO: Create
# * private
class PrivatyPoliceListView(CreateAPIView):
   queryset = all_privaty_police_service()
   serializer_class = PrivatyPoliceSerializer

# ! /private-policy/:id
# TODO:  Show, Update
# * public(get) private(update)
class PrivatyPoliceDetailView(RetrieveUpdateAPIView):
   queryset = all_privaty_police_service()
   serializer_class = PrivatyPoliceSerializer