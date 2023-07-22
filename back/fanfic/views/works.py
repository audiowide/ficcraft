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
                                   HTTP_404_NOT_FOUND, 
                                   HTTP_204_NO_CONTENT)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from base.utils import AdminPermission, CreateOnlyPermission

from ..models import Work, Chapter
from django.contrib.auth.models import User
from ..serializers import WorkSerializer, CreateWorkSerializer, ChapterSerializer
from ..services import all_works_service

from ..utils import slug_generator
from user.models import Profile

from django.core.paginator import Paginator
from rest_framework.pagination import PageNumberPagination


# ! /works
# TODO: Show All and Create
# * public / private
@api_view(['GET', 'POST'])
def show_all_works(request):
   if request.method == 'GET':
      works = Work.objects.all()
      
      title = request.GET.get('title', '')
      user = request.GET.get('user', '')
      workType = request.GET.get('workType', '')
      fanfic_type = request.GET.get('fanficType', '')
      
      fandoms = request.GET.get('fandoms')
      characters = request.GET.get('characters', '')
      pairings = request.GET.get('pairings', '')
      tags = request.GET.get('tags', '')
      
      raiting = request.GET.get('raiting', '')
      orientation = request.GET.get('orientation', '')
      progressType = request.GET.get('progressType', '')
      
      progressType = request.GET.get('progressType', '')
      size = request.GET.get('size', 10)
            
      if title:
         works = works.filter(title__icontains=title)
      if user:
         works = works.filter(user__username__icontains=user)
      if workType:
         works = works.filter(workType=workType)
      if fanfic_type:
         works = works.filter(fanfic_type=fanfic_type)
      if fandoms:
         works = works.filter(fandoms__name__icontains=fandoms)
      if characters:
         works = works.filter(characters__name__icontains=characters)
      if pairings:
         works = works.filter(pairings__name__icontains=pairings)
      if tags:
         works = works.filter(tags__name__icontains=tags)
      if raiting:
         works = works.filter(raiting=raiting)
      if orientation:
         works = works.filter(orientation=orientation)
      if progressType:
         works = works.filter(progressType=progressType)
               
      works = works.distinct()
      
      paginator = Paginator(works, size)
      
      page_number = request.GET.get('page', 1)
      
      page_obj = paginator.get_page(page_number)
      
      return Response({
         'page': int(page_number),
         'size': int(size),
         'totalElements': works.count(),
         'content': WorkSerializer(page_obj, many=True).data
      }, status=HTTP_200_OK)
   if request.method == 'POST':
      if request.user.is_authenticated:
         title = request.data.get('title')

         data = {
            'title': title,
            'slug': slug_generator(title),
            # 'image': request.FILES.get('image', 'book.jpeg' ),
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
         work = serializer.save()
         
         work.image = request.FILES.get('image', 'book.jpeg' )
         work.save()
         
         
         return Response({
               'status': 'success',
               'slug': work.slug,
            }, status=HTTP_201_CREATED)

# ! /works/:slug
# TODO: Show One Work
# * public
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
      
               work.title =  title,
               work.slug = slug_generator(title),
               work.image = request.FILES.get('image', 'book.jpeg'),
               work.workType =  request.data['workType'],
               work.fanfic_type = request.data['fanfic_type'],
                  
               work.fandoms = request.data['fandoms'],
               work.characters =  request.data['characters'],
               work.pairings = request.data['pairings'],
                  
               work.raiting = request.data['raiting'],
               work.orientation = request.data['orientation'],
                  
               work.tags = request.data['tags'],
               work.description = request.data['description'],
               work.notes = request.data['notes'],
               work.progressType = request.data['progressType'],
               work.public = request.data['public'],
               
               work.save()
               
               return Response({
                     'work': work
                  }, status=201)
         
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /works/:slug/add-to-lower
# TODO: Add To Lower
# * private
@api_view(['POST'])
def  add_to_lowe_one_work(request, slug):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
   if request.method == 'POST':
      if request.user.is_authenticated:
         profile = Profile.objects.get(user=request.user)
         
         if profile.lowers.filter(pk=work.pk).exists():
            profile.lowers.remove(work)
            return Response({
               'message': 'Unlicked successfully'
            }, status=HTTP_200_OK)
         else:
            profile.lowers.add(work)
            return Response({
               'message': 'Liked successfully'
            }, status=HTTP_200_OK)

# ! /works/:slug/chapters
# TODO: Show All
# * public
@api_view(['GET', 'POST'])
def chapters_view(request, slug):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
      
      if request.method == 'GET':
         chapters = Chapter.objects.filter(work=work).order_by('place')
      
         return Response({
            'chapters_count': chapters.count(),
            'chapters': ChapterSerializer(chapters, many=True).data
         }, status=HTTP_200_OK)
         
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
                  'place': Chapter.objects.filter(work=work).count() + 1,
                  
                  'public': request.data['public'],
               }

               serializer = ChapterSerializer(data=data)
               serializer.is_valid(raise_exception=True)
               chapter = serializer.save()
               
               return Response({
                     'chapter': ChapterSerializer(chapter, many=False).data
                  }, status=HTTP_201_CREATED)
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
      
# ! /works/:slug/chapters/:id
# TODO: Show One, Update, Delete
# * public/private
@api_view(['GET', 'PUT', 'DELETE'])
def chapter_view(request, slug, pk):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
      chapter = Chapter.objects.get(id=pk)
      
      if request.method == 'GET':
         return Response({
            'chapter': ChapterSerializer(chapter, many=False).data
         }, status=HTTP_200_OK)
      
      if request.user.is_authenticated:
         if request.user == work.user:
            if request.method == 'DELETE':
               chapter.delete()
               return Response({
                  'message': 'Deleted successfully'
               }, status=HTTP_204_NO_CONTENT)
               
            if request.method == 'PUT':
               chapter.title = request.data['title']
               chapter.after_text = request.data['after_text']
               chapter.pre_text = request.data['pre_text']
               chapter.text = request.data['text']
               chapter.text = request.data['public']
               
               chapter.save()
               return Response({
                  'chapter': ChapterSerializer(chapter, many=False).data
               }, status=HTTP_200_OK)
         
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# TODO: Change Place
# * private
@api_view([ 'PUT'])
def chapter_place_view(request, slug, pk):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
      chapter = Chapter.objects.get(id=pk)
      
      if request.user.is_authenticated:
         if request.user == work.user:
            if request.method == 'PUT':
               
               chapter.place = request.data['place']
               
               chapter.save()
               return Response({
                  'chapter': ChapterSerializer(chapter, many=False).data
               }, status=HTTP_200_OK)
         
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /works/:slug/add-to-lower/:id
# TODO: Add To Bookmarks 
# * private
@api_view(['POST'])
def  add_to_bookmarks_one_chapter(request, slug, chapter_id):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
      chapter = Chapter.objects.get(id=chapter_id)

   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
   if request.method == 'POST':
      if request.user.is_authenticated:
         profile = Profile.objects.get(user=request.user)
         
         if profile.bookmarks.filter(pk=chapter.pk).exists():
            profile.bookmarks.remove(chapter)
            return Response({
               'message': 'Unlicked successfully'
            }, status=HTTP_200_OK)
         else:
            profile.bookmarks.add(chapter)
            return Response({
               'message': 'Liked successfully'
            }, status=HTTP_200_OK)