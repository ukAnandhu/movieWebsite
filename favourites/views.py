from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from favourites.models import Favourite
from movies.models import Movie
# Create your views here.


@login_required
def add_to_favourites(request,movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    favourite, created = Favourite.objects.get_or_create(user=request.user, movie=movie)
    if created:
        return redirect('movie_detail',movie_id=movie.id)

@login_required
def favourite_movies(request):
    favourites = Favourite.objects.filter(user=request.user).select_related('movie')

    return render(request,'fav/favourites.html',{'favourites':favourites})