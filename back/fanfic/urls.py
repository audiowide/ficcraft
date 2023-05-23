from django.urls import path
from .views import categories

urlpatterns = [
   # ?  tags
   path('tags', categories.TagListCreateView.as_view()),
   path('tags/<int:pk>/', categories.TagDetailView.as_view()),
]
