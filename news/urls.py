from django.urls import path
from . import views

urlpatterns = [
    path('bbc', views.BbcNewsView.as_view(), name='bbc'),
    path('bbc/<int:pk>', views.BbcNewsDetailView.as_view()),
    path('hackernews', views.HackerNewsView.as_view(), name='hacker'),
    path('hackernews/<int:pk>', views.HackerNewsDetailView.as_view())
]