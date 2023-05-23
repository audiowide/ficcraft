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
from ..services import all_tags_service


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