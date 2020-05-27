from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="posts-home"),
    path('about/', views.about, name="posts-about"),
    path('createpost/', views.createPost, name="posts-create"),
    path('editpost/<int:post_id>', views.editPost, name="posts-edit"),
    path('deletepost/<int:post_id>', views.deletePost, name="posts-delete"),
    path('filters/', views.filters, name="filters"),
]


# URL patterns
# 'xyz/<type:var_name>/'