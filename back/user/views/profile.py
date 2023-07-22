from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_404_NOT_FOUND, 
                                   HTTP_204_NO_CONTENT)
from django.contrib.auth.hashers import make_password

from ..serializers import UserSerializer, ProfileSerializer, CollectionSerializer
from fanfic.serializers import (WorkSerializer, 
                                WorkCommentSerializer, 
                                ChapterCommentSerializer)

from ..models import Profile, User, Collection
from fanfic.models import Work, WorkComment, ChapterComment


# ! /profile/:username
# TODO: Show Profile / Update Profile
# * public / private
@api_view(['GET', 'PUT'])
def show_profile_view(request, username):
   try:
      user = User.objects.get(username=username)
      profile = Profile.objects.get(user=user)
      
      if request.method == 'GET':
         return Response(ProfileSerializer(profile, many=False).data, 
                         status = HTTP_200_OK)
         
      if request.method == 'PUT':
         if request.user.is_authenticated:
            if request.user == user:
               profile.avatar =  request.FILES.get('avatar')
               profile.background = request.FILES.get('background')
               profile.about = request.data.get('about')
               
               profile.save()
               return Response(ProfileSerializer(profile, many=False).data, 
                              status=HTTP_200_OK)
   
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /profile/:username/update-email
# TODO: Update email
# *  private
@api_view(['PUT'])
def profile_update_email_view(request, username):
   try:
      user = User.objects.get(username=username)
      profile = Profile.objects.get(user=user)
         
      if request.method == 'PUT':
         if request.user.is_authenticated:
            if request.user == user:
               user.email = request.data.get('email')
               
               user.save()
                             
               return Response({
                        'message': 'Email changed successfully'
                     }, status=HTTP_200_OK)
   
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /profile/:username/update-password
# TODO: Update password
# *  private
@api_view(['PUT'])
def profile_update_password_view(request, username):
   try:
      user = User.objects.get(username=username)
      profile = Profile.objects.get(user=user)
         
      if request.method == 'PUT':
         if request.user.is_authenticated:
            if request.user == user:
               password = request.data.get('password')
               password_confirmation = request.data.get('password_confirmation')
               
               if password == password_confirmation:
                  if password != user.password:
                     user.password = make_password(password)
                     user.save()
                     
                     return Response({
                        'message': 'Password changed successfully'
                     }, status=HTTP_200_OK)
                  else:
                     return Response({'message': 'password is incorrect'},
                       status=HTTP_400_BAD_REQUEST)
               else:
                  return Response({'message': 'password confirmation does not match password'},
                       status=HTTP_400_BAD_REQUEST)
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
   
# ! /profile/:username/works
# TODO: Show all works
# *  public
@api_view(['GET'])
def show_user_works_view(request, username):
   try:
      user = User.objects.get(username=username)
      works = Work.objects.filter(user=user)

      return Response(WorkSerializer(works, many=True).data, 
                      status=HTTP_200_OK)
       
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
    
# ! /profile/:username/collections
# TODO: Create And Show All collection
# *  private  / public
@api_view(['GET', 'POST'])
def show_user_collections_view(request, username):
   try:
      user = User.objects.get(username=username)
      collections = Collection.objects.filter(user=user)

      if request.method == 'GET': 
         return Response(CollectionSerializer(collections, many=True).data, 
                      status=HTTP_200_OK)
      if request.method == 'POST':
        if request.user == user:
            title = request.data.get('title')
            public = request.data.get('public')
            
            collection = Collection.objects.create(
               user = user,
               title = title,
               public = public
            )
            
            collection.save()
            return Response(CollectionSerializer(collection, many=False).data, 
                           status=HTTP_201_CREATED)
       
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /profile/:username/collections/:id
# TODO: Show One Collection / Update / Delete
# *  private  / public
@api_view(['GET', 'PUT', 'DELETE'])
def show_user_collection_view(request, username, pk):
   try:
      user = User.objects.get(username=username)
      collection = Collection.objects.get(id=pk)

      if request.method == 'GET': 
         return Response(CollectionSerializer(collection, many=False).data, 
                      status=HTTP_200_OK)
         
      if request.method == 'PUT':
        if request.user == user:
            collection.title = request.data.get('title')
            collection.public = request.data.get('public')
            
            collection.save()
            return Response(CollectionSerializer(collection, many=False).data, 
                           status=HTTP_200_OK)
            
      if request.method == 'DELETE':
         if request.user == user:
            collection.delete()
            return Response({
               'message': 'Deleted successfully'
            }, status=HTTP_200_OK)
            
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /profile/:username/comments
# TODO: Show All Comments
# *  public
@api_view(['GET'])
def show_user_comments_view(request, username):
   try:
      user = User.objects.get(username=username)
      
      workComments = WorkComment.objects.filter(user=user)
      chapterComments = ChapterComment.objects.filter(user=user)
      
      if request.method == 'GET':
         return Response({
            'workComments': WorkCommentSerializer(workComments, many=True).data,
            'chapterComments': ChapterCommentSerializer(chapterComments, many=True).data,
         }, status=HTTP_200_OK)
       
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /profile/:username/lowers
# TODO: Show All Lowers
# *  public
@api_view(['GET'])
def show_user_lowers_view(request, username):
   try:
      user = User.objects.get(username=username)
      profile = Profile.objects.get(user=user)
      
      if request.method == 'GET':
         return Response({
            'count': profile.lowers.count(),
           'lowers': WorkSerializer(profile.lowers, many=True).data
         }, status=HTTP_200_OK)
       
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
      
# ! /profile/:username/delete
# TODO: Delete Account
# *  private
@api_view(['DELETE'])
def profile_delete_view(request, username):
   try:
      user = User.objects.get(username=username)
      profile = Profile.objects.get(user=user)
         
      if request.method == 'PUT':
         if request.user.is_authenticated:
            if request.user == user:
               profile.delete()
               user.delete()
               
               return Response({
                  'message': 'Profile deleted successfully'
                  }, status=HTTP_200_OK)
   
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)