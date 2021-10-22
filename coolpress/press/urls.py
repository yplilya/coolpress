from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.post_detail, name='posts-detail'),
    path('posts/', views.post_list, name='posts-list'),
]