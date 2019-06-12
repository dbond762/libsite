from django.urls import path

from library import views

app_name = 'library'
urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.authors, name='authors'),
    path('genres/', views.genres, name='genres'),
    path('forms/', views.forms, name='forms'),
]
