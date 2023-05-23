from django.urls import path
from .views import news_view, info_view

urlpatterns = [
    # ?  news
    path('news', news_view.NewsListView.as_view()),
    path('news/<int:pk>/', news_view.NewsDetailView.as_view()),
    
    # ? about
    path('about', info_view.AboutListView.as_view()),
    path('about/<int:pk>/', info_view.AboutDetailView.as_view()),
    
    # ?  fanfic rool
    path('fanfic-rool', info_view.FanficRoolListView.as_view()),
    path('fanfic-rool/<int:pk>/', info_view.FanficRoolDetailView.as_view()),
    
    # ?  faq
    path('faq', info_view.FaqListCreateAPIView.as_view()),
    path('faq/<int:pk>/', info_view.FaqDetailView.as_view()),
    
    # ?  private policy
    path('private-policy', info_view.PrivatyPoliceListView.as_view()),
    path('private-policy/<int:pk>', info_view.PrivatyPoliceDetailView.as_view()),
]