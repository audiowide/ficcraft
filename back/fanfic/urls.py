from django.urls import path

from .views import (categories, 
                    works, 
                    comments)

urlpatterns = [
   # ?  tags
   path('tags', categories.TagListCreateView.as_view()),
   path('tags/<int:pk>/', categories.TagDetailView.as_view()),
   
   # ?  fandoms
   path('fandoms', categories.FandomListCreateView.as_view()),
   path('fandoms/<int:pk>/', categories.FandomDetailView.as_view()),
   path('fandoms/<int:pk>/add-to-lower', categories.add_fandom_to_bookmark),
   
    # ?  characters
   path('characters', categories.CharacterListCreateView.as_view()),
   path('characters/<int:pk>/', categories.CharacterDetailView.as_view()),
   path('characters/<int:pk>/add-to-lower', categories.add_characters_to_bookmark),
   
   # ?  pairings
   path('pairings', categories.PairingListCreateView.as_view()),
   path('pairings/<int:pk>/', categories.PairingDetailView.as_view()),
   path('pairings/<str:slug>/add-to-lower', categories.add_pairings_to_bookmark),
   
   # ? works
   path('works', works.show_all_works),
   path('works/<str:slug>/', works.show_one_work),
   path('works/<str:slug>/add-to-lower', works.add_to_lowe_one_work),
   
   # path('works', works.WorkCreateView.as_view()),
   # path('works/<str:slug>/', works.WorksDetailView.as_view()),

   # ? chapters
   path('works/<str:slug>/chapters', works.chapters_view),
   path('works/<str:slug>/chapters/<int:pk>', works.chapter_view),
   path('works/<str:slug>/chapters/<int:chapter_id>/add-to-lower', works.add_to_bookmarks_one_chapter),
   path('works/<str:slug>/chapters/<int:pk>/place-edit', works.chapter_place_view),
   
   # ? work comments
   path('works/<str:slug>/comments', comments.work_comments_view),
   path('works/<str:slug>/comments/<int:pk>', comments.work_comment_view),
   
]
