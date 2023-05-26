from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     CreateAPIView, 
                                     ListAPIView, 
                                     RetrieveDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_404_NOT_FOUND)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from base.utils import AdminPermission, CreateOnlyPermission

from ..models import Work, Chapter
from django.contrib.auth.models import User
from ..serializers import WorkSerializer, CreateWorkSerializer, ChapterSerializer
from ..services import all_works_service

from user.utils import auth_check
from ..utils import slug_generator


# ! /works
# TODO: Show All
# * public
@api_view(['GET', 'POST'])
def show_all_works(request):
   if request.method == 'GET':
      works = Work.objects.all()
   
      return Response({
         'works': WorkSerializer(works, many=True).data
      }, status=HTTP_200_OK)
   if request.method == 'POST':
      if request.user.is_authenticated:
         title = request.data.get('title')
         
         data = {
            'title': title,
            'slug': slug_generator(title),
            'image': request.FILES.get('image', 'book.jpeg'),
            'user': request.user.id,
            'workType': request.data['workType'],
            'fanfic_type': request.data['fanfic_type'],
            
            'fandoms': request.data['fandoms'],
            'characters': request.data['characters'],
            'pairings': request.data['pairings'],
            
            'raiting': request.data['raiting'],
            'orientation': request.data['orientation'],
            
            'tags': request.data['tags'],
            'description': request.data['description'],
            'notes': request.data['notes'],
            'progressType': request.data['progressType'],
            'public': False
         }

         serializer = CreateWorkSerializer(data=data)
         serializer.is_valid(raise_exception=True)
         work = serializer.create(serializer.validated_data)
         
         return Response({
               'work': work
            }, status=HTTP_201_CREATED)
      

# # ! /works
# # TODO: Create
# # * private
# class WorkCreateView(CreateAPIView):
#    queryset = all_works_service()
#    serializer_class = CreateWorkSerializer
#    permission_classes =  [CreateOnlyPermission]
   
#    def perform_create(self, serializer):
#       serializer.save(slug=slug_generator(serializer.validated_data['title']),
#                         user=self.request.user)

# # ! /works/:id
# # TODO: Show One Work
# # * public
@api_view(['GET', 'PUT', 'DELETE'])
def  show_one_work(request, slug):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
      
      if request.method == 'GET':
         return Response({
            'work': WorkSerializer(work, many=False).data
         }, status=HTTP_200_OK)
         
         if request.user.is_authenticated:
            if request.user == work.user:
               if request.method == 'DELETE':
                  work.delete()
                  return Response({
                     'message': 'Work deleted'
                  }, status=HTTP_200_OK)
                  
               if request.method == 'PUT':
                  title = request.data.get('title')
         
                  data = {
                     'title': title,
                     'slug': slug_generator(title),
                     'image': request.FILES.get('image', 'book.jpeg'),
                     'user': request.user.id,
                     'workType': request.data['workType'],
                     'fanfic_type': request.data['fanfic_type'],
                     
                     'fandoms': request.data['fandoms'],
                     'characters': request.data['characters'],
                     'pairings': request.data['pairings'],
                     
                     'raiting': request.data['raiting'],
                     'orientation': request.data['orientation'],
                     
                     'tags': request.data['tags'],
                     'description': request.data['description'],
                     'notes': request.data['notes'],
                     'progressType': request.data['progressType'],
                     'public': request.data['public'],
                  }

                  serializer = CreateWorkSerializer(data=data)
                  serializer.is_valid(raise_exception=True)
                  work = serializer.create(serializer.validated_data)
                  
                  return Response({
                        'work': work
                     }, status=201)
         
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)

# ! /works/:id/chapters/:id
# TODO: Show All
# * public
@api_view(['GET', 'POST'])
def chapters_view(request):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
      
      if request.method == 'GET':
         chapters = Chapter.objects.filter(work=work)
      
         return Response([
            ''
         ])
      if request.method == 'POST':
         if request.user.is_authenticated:
            if request.user == work.user:
               data = {
                  'user': request.user.id,
                  'work': work.id,
                  'title': request.data['title'],
                  
                  'pre_text': request.data['pre_text'],
                  'text': request.data['text'],
                  'after_text': request.data['after_text'],
                  
                  'public': request.data['public'],
               }

               serializer = ChapterSerializer(data=data)
               serializer.is_valid(raise_exception=True)
               chapter = serializer.create(serializer.validated_data)
               
               return Response({
                     'chapter': chapter
                  }, status=HTTP_201_CREATED)
            
         
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)