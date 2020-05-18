from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="posts-home"),
    path('about/', views.about, name="posts-about"),
    path('createpost/', views.createPost, name="posts-create"),
]
#  about/
