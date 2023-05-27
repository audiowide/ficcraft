from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_404_NOT_FOUND, 
                                   HTTP_204_NO_CONTENT)

from ..models import ChapterComment, WorkComment, Work, Chapter
from django.contrib.auth.models import User
from ..serializers import (WorkCommentSerializer, 
                           CreateWorkCommentSerializer,
                           ChapterCommentSerializer, 
                           CreateWorkCommentNotParrentSerializer)
from ..services import all_work_comments_service, all_chapter_comments_service

# ! /works/:slug/comments
# TODO: Show All and create new
# * public/private
@api_view(['GET', 'POST'])
def work_comments_view(request, slug):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
      
      if request.method == 'GET':
         comments = WorkComment.objects.filter(work=work, parent=None)
      
         return Response({
            'comments_count': comments.count(),
            'comments': WorkCommentSerializer(comments, many=True).data
         }, status=HTTP_200_OK)
         
      if request.method == 'POST':
         if request.user.is_authenticated:
            parent_id = request.data.get('parent')
            
            data = {
               'user': request.user.id,
               'work': work.id,
              
              'parent': '',
              'body': request.data['body'],
            }
            
            if parent_id:
               try:
                     parent_comment = WorkComment.objects.get(id=parent_id)
                     data['parent'] = parent_comment.id
                     
                     serializer = CreateWorkCommentSerializer(data=data)
               except WorkComment.DoesNotExist:
                     raise serializers.ValidationError("Invalid parent comment ID.")
            else:
               parent_comment = None
               data['parent'] = parent_comment
               
               serializer = CreateWorkCommentNotParrentSerializer(data=data)
               
            serializer.is_valid(raise_exception=True)
            comment = serializer.save()
            
            return Response({
                  'comment': WorkCommentSerializer(comment, many=False).data
               }, status=HTTP_201_CREATED)
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /works/:slug/comments/:id
# TODO: Update / Delete
# * public/private
@api_view(['PUT', 'DELETE'])
def work_comment_view(request, slug, pk):
   try:
      # get one work
      work = Work.objects.get(slug=slug)
      comment = WorkComment.objects.get(id=pk)
      
      if request.user.is_authenticated:
         if request.user == comment.user:
            if request.method == 'PUT':
               comment.body = request.data['body']
               comment.save()
               
               return Response({
                     'comment': WorkCommentSerializer(comment, many=False).data
                  }, status=HTTP_200_OK)
            if request.method == 'DELETE':
               comment.delete()
               
               return Response({
                     'message': 'comment deleted successfully'
                  }, status=HTTP_200_OK)
            
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)