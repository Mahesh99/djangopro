from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="posts-home"),
    path('about/', views.about, name="posts-about"),
]
#  about/
