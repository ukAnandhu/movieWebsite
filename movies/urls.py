
from django.urls import path
from .views import search_movies,add_movie, edit_movie, delete_movie, movie_list, movie_detail

urlpatterns = [

    path('movies/add/', add_movie, name='add_movie'),
    path('movies/edit/<int:movie_id>/', edit_movie, name='edit_movie'),
    path('movies/delete/<int:movie_id>/', delete_movie, name='delete_movie'),
    path('', movie_list, name='movie_list'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('category/<slug:category_slug>/', movie_list, name='category_list'),
    path('search/', search_movies, name='search_movies'),
    
]
