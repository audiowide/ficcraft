from django.urls import path

from .views import categories
from .views import works

urlpatterns = [
   # ?  tags
   path('tags', categories.TagListCreateView.as_view()),
   path('tags/<int:pk>/', categories.TagDetailView.as_view()),
   
   # ?  fandoms
   path('fandoms', categories.FandomListCreateView.as_view()),
   path('fandoms/<int:pk>/', categories.FandomDetailView.as_view()),
   
    # ?  characters
   path('characters', categories.CharacterListCreateView.as_view()),
   path('characters/<int:pk>/', categories.CharacterDetailView.as_view()),
   
   # ?  pairings
   path('pairings', categories.PairingListCreateView.as_view()),
   path('pairings/<int:pk>/', categories.PairingDetailView.as_view()),
   
   # ? works
   path('works', works.show_all_works),
   # path('works', works.WorkCreateView.as_view()),
   path('works/<str:slug>/', works.show_one_work),
   # path('works/<str:slug>/', works.WorksDetailView.as_view()),
]
