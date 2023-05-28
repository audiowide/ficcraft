from django.urls import path

from .views import auth, profile

urlpatterns = [
   # auth
   path('auth/sign-up', auth.sign_up_view, name='sign-up'),
   path('auth/sign-in', auth.sign_in_view, name='sign-in'),
   path('auth/sign-out', auth.sign_out_view, name='sign-out'),
   
   # profile
   path('profile/<str:username>', profile.show_profile_view),
   path('profile/<str:username>/works', profile.show_user_works_view),
   path('profile/<str:username>/collections', profile.show_user_collections_view),
]