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
   path('profile/<str:username>/comments', profile.show_user_comments_view),
   path('profile/<str:username>/lowers', profile.show_user_lowers_view),
   
   # DANGER ZONE 
   path('profile/<str:username>/update-email', profile.profile_update_email_view),
   path('profile/<str:username>/update-password', profile.profile_update_password_view),
   path('profile/<str:username>/delete', profile.profile_delete_view),
   
   # collections
   path('profile/<str:username>/collections', profile.show_user_collections_view),
   path('profile/<str:username>/collections/<int:pk>', profile.show_user_collection_view),
   
]