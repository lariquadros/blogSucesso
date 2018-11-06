from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('comentario/' , views.comentario_new, name='comentario_new'),
    path('comentario/<int:pk>/delete/', views.comentario_delete, name='comentario_delete'),
    path('comentario/<int:pk>/edit/', views.comentario_edit, name='comentario_edit'),
]