from django.urls import path

from library import views

app_name = 'library'
urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.authors, name='authors'),
    path('genres/', views.genres, name='genres'),
    path('forms/', views.forms, name='forms'),
]
