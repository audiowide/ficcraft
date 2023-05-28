from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import (HTTP_200_OK, 
                                   HTTP_201_CREATED, 
                                   HTTP_404_NOT_FOUND, 
                                   HTTP_204_NO_CONTENT)

from ..serializers import UserSerializer, ProfileSerializer, CollectionSerializer
from fanfic.serializers import WorkSerializer

from ..models import Profile, User, Collection
from fanfic.models import Work


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
      
@api_view(['GET'])
def show_user_collections_view(request, username):
   try:
      user = User.objects.get(username=username)
      collections = Collection.objects.filter(user=user)

      return Response(CollectionSerializer(collections, many=True).data, 
                      status=HTTP_200_OK)
       
   except:
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)