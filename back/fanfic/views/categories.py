from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     CreateAPIView, 
                                     ListAPIView, 
                                     RetrieveDestroyAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from base.utils import AdminPermission, CreateOnlyPermission

from ..serializers import (TagSerializer, 
                           FandomSerializer, 
                           CharacterSerializer, 
                           PairingSerializer, 
                           CreatePairingSerializer,
                           WorkSerializer, 
                           CreateCharacterSerializer)
from ..services import (all_tags_service, 
                        all_fandoms_service, 
                        all_characters_service, 
                        all_pairings_service)

from ..models import (Work)

from ..models import (Fandom, Character, Pairing)


# ! /tags
# TODO: Show All and Create
# * public(tags), private(create)
class TagListCreateView(ListCreateAPIView):
   queryset = all_tags_service()
   serializer_class = TagSerializer
   permission_classes =  [CreateOnlyPermission]
      
# ! /tags/:id
# TODO: Show One, Update, Destroy
# * public(show one), private(update, destroy)
class TagDetailView(RetrieveUpdateDestroyAPIView):
   queryset = all_tags_service()
   serializer_class = TagSerializer
   permission_classes =  [CreateOnlyPermission]
   
   def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      works =  Work.objects.filter(tags=instance)
      works_serializer = WorkSerializer(works, many=True)
      serialized_data = serializer.data
      serialized_data['works'] = works_serializer.data
      return Response(serialized_data)
      
# ! /fandoms
# TODO: Show All and Create
# * public(show all), private(create)
class FandomListCreateView(ListCreateAPIView):
   queryset = all_fandoms_service()
   serializer_class = FandomSerializer
   permission_classes =  [CreateOnlyPermission]
   
# ! /fandoms/:id
# TODO: Show One, Update, Destroy
# * public(show one), private(update, destroy)
class FandomDetailView(RetrieveUpdateDestroyAPIView):
   queryset = all_fandoms_service()
   serializer_class = FandomSerializer
   permission_classes =  [CreateOnlyPermission]
   
   def get_serializer_class(self):
      if self.request.method == 'PUT':
         return  CreateCharacterSerializer
      return super().get_serializer_class()
   
   def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      print(instance)
      works =  Work.objects.filter(fandoms=instance)
      works_serializer = WorkSerializer(works, many=True)
      serialized_data = serializer.data
      serialized_data['works'] = works_serializer.data
      return Response(serialized_data)
   
# ! /fandoms/:id/add-to-lower
# TODO: Add Fandom To Lower
# * private
@api_view(['POST'])
def  add_fandom_to_bookmark(request, slug):
   try:
      # get one work
      fandom = Fandom.objects.get(slug=slug)
      
      if request.method == 'POST':
         if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            
            if profile.fandom_bookmarks.filter(fandom=fandom):
               profile.fandom_bookmarks.remove(fandom.id)
               
               return Response({
                  'message': 'Fandom Unbookmarked Successfully'
               }, status=HTTP_200_OK)
            else:
               profile.fandom_bookmarks.add(fandom.id)
               
               return Response({
                  'message': 'Fandom Bookmarked Successfully'
               }, status=HTTP_200_OK)
      
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
   
# ! /characters
# TODO: Show All and Create
# * public(show all), private(create)
class CharacterListCreateView(ListCreateAPIView):
   queryset = all_characters_service()
   serializer_class = CharacterSerializer
   permission_classes =  [CreateOnlyPermission]
   
   def get_serializer_class(self):
      if self.request.method == 'POST':
         return  CreateCharacterSerializer
      return super().get_serializer_class()
   
# ! /characters/:id
# TODO: Show One, Update, Destroy
# * public(show one), private(update, destroy)
class CharacterDetailView(RetrieveUpdateDestroyAPIView):
   queryset = all_characters_service()
   serializer_class = CharacterSerializer
   permission_classes =  [CreateOnlyPermission]
   
   def get_serializer_class(self):
      if self.request.method == 'PUT':
         return  CreateCharacterSerializer
      return super().get_serializer_class()
   
   def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      works =  Work.objects.filter(characters=instance)
      works_serializer = WorkSerializer(works, many=True)
      serialized_data = serializer.data
      serialized_data['works'] = works_serializer.data
      return Response(serialized_data)
   
# ! /characters/:id/add-to-lower
# TODO: Add Characters To Lower
# * private
@api_view(['POST'])
def  add_characters_to_bookmark(request, slug):
   try:
      # get one work
      character = Character.objects.get(slug=slug)
      
      if request.method == 'POST':
         if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            
            if profile.character_bookmarks.filter(character=character):
               profile.character_bookmarks.remove(character.id)
               
               return Response({
                  'message': 'Character Unbookmarked Successfully'
               }, status=HTTP_200_OK)
            else:
               profile.character_bookmarks.add(character.id)
               
               return Response({
                  'message': 'Character Bookmarked Successfully'
               }, status=HTTP_200_OK)
      
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)
   
# ! /pairings
# TODO: Show All and Create
# * public(show all), private(create)
class PairingListCreateView(ListCreateAPIView):
   queryset = all_pairings_service()
   serializer_class = PairingSerializer
   permission_classes =  [CreateOnlyPermission]
   
   def get_serializer_class(self):
      if self.request.method == 'POST':
         return  CreatePairingSerializer
      return super().get_serializer_class()
   
# ! /pairings/:id
# TODO: Show One, Update, Destroy
# * public(show one), private(update, destroy)
class PairingDetailView(RetrieveUpdateDestroyAPIView):
   queryset = all_pairings_service()
   serializer_class = PairingSerializer
   permission_classes =  [CreateOnlyPermission]
   
   def get_serializer_class(self):
      if self.request.method == 'PUT':
         return  CreatePairingSerializer
      return super().get_serializer_class()
   
   def retrieve(self, request, *args, **kwargs):
      instance = self.get_object()
      serializer = self.get_serializer(instance)
      works =  Work.objects.filter(pairings=instance)
      works_serializer = WorkSerializer(works, many=True)
      serialized_data = serializer.data
      serialized_data['works'] = works_serializer.data
      return Response(serialized_data)
   
# ! /pairings/:id/add-to-lower
# TODO: Add Pairing To Lower
# * private
@api_view(['POST'])
def  add_pairings_to_bookmark(request, slug):
   try:
      # get one work
      pairing = Pairing.objects.get(slug=slug)
      
      if request.method == 'POST':
         if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            
            if profile.pairing_bookmarks.filter(pairing=pairing):
               profile.pairing_bookmarks.remove(pairing.id)
               
               return Response({
                  'message': 'Pairing Unbookmarked Successfully'
               }, status=HTTP_200_OK)
            else:
               profile.pairing_bookmarks.add(pairing.id)
               
               return Response({
                  'message': 'Pairing Bookmarked Successfully'
               }, status=HTTP_200_OK)
      
   except:
      # show message if work is not found
      return Response({
         'detail': 'Not found.'
         }, status=HTTP_404_NOT_FOUND)