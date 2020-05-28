from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="posts-home"),
    path('about/', views.about, name="posts-about"),
    path('createpost/', views.createPost, name="posts-create"),
    path('editpost/<int:post_id>', views.editPost, name="posts-edit"),
    path('deletepost/<int:post_id>', views.deletePost, name="posts-delete"),
    path('filters/', views.filters, name="filters"),

    # class based views 
    path('home/',views.PostListView.as_view(), name="home"),
    path('post/<int:pk>',views.PostDetailView.as_view(), name="detail"),
    path('post/create/',views.PostCreateView.as_view(), name="create"),
    path('post/<int:pk>/update',views.PostUpdateView.as_view(), name="update"),
    path('post/<int:pk>/delete',views.PostDeleteView.as_view(), name="delete"),

]


# URL patterns
# 'xyz/<type:var_name>/'