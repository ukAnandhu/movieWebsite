from django.urls import path
from .import views

urlpatterns = [
    path('movies/<int:movie_id>/add_favourites/',views.add_to_favourites,name='add_to_favourites'),
    path('favourites/',views.favourite_movies,name='favourite_movies')
]