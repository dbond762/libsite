from django.urls import path

from library import views

app_name = 'library'
urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:book_id>/vote/', views.vote, name='vote'),
    path('authors/', views.authors, name='authors'),
    path('authors/<int:pk>/', views.author_books, name='author_books'),
    path('genres/', views.genres, name='genres'),
    path('forms/', views.forms, name='forms'),
]
