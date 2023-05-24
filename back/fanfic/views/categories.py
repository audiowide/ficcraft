from rest_framework.decorators import api_view
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from base.utils import AdminPermission, CreateOnlyPermission

from ..serializers import (TagSerializer, 
                           FandomSerializer, 
                           CharacterSerializer, 
                           PairingSerializer, 
                           WorkSerializer)
from ..services import (all_tags_service, 
                        all_fandoms_service, 
                        all_characters_service)


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
   
# ! /characters
# TODO: Show All and Create
# * public(show all), private(create)
class CharacterListCreateView(ListCreateAPIView):
   queryset = all_characters_service()
   serializer_class = CharacterSerializer
   permission_classes =  [CreateOnlyPermission]
   
# ! /characters/:id
# TODO: Show One, Update, Destroy
# * public(show one), private(update, destroy)
class CharacterDetailView(RetrieveUpdateDestroyAPIView):
   queryset = all_characters_service()
   serializer_class = CharacterSerializer
   permission_classes =  [CreateOnlyPermission]