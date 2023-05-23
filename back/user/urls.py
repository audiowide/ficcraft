from django.urls import path
from .views import auth

urlpatterns = [
   path('auth/sign-up', auth.sign_up_view, name='sign-up'),
   path('auth/sign-in', auth.sign_in_view, name='sign-in'),
   path('auth/sign-out', auth.sign_out_view, name='sign-out'),
]