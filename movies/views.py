from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from accounts.forms import CustomUserCreationForm
from favourites.models import Favourite
from .forms import MovieForm, ReviewForm
from .models import Movie, Category, Review
from django.core.paginator import Paginator
from django.db.models import Q


@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

@login_required
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id, user=request.user)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/edit_movie.html', {'form': form})

@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id, user=request.user)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/delete_movie.html', {'movie': movie})

def movie_list(request,category_slug=None):
    categories = None
    object_list = None
    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        object_list = Movie.objects.filter(category=categories,is_available=True)
    else:
        object_list = Movie.objects.all().filter(is_available=True)
    paginator = Paginator(object_list, 6)  

    page_number = request.GET.get('page')
    movies = paginator.get_page(page_number)
    context = {        
            'movies':movies
        }
    # movies = Movie.objects.all()
    # categories = Category.objects.all()
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    is_favourite = False
    if request.user.is_authenticated:
        is_favourite = Favourite.objects.filter(user=request.user, movie=movie).exists()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        form = ReviewForm()
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'reviews': reviews, 'form': form,'is_favourite':is_favourite})

# def category_list(request, category_id):
#     category = get_object_or_404(Category, pk=category_id)
#     movies = Movie.objects.filter(category=category)
#     categories = Category.objects.all()
#     return render(request, 'category_list.html', {'movies': movies, 'categories': categories, 'category': category})


def search_movies(request):
    keyword = request.GET.get('keyword','')
    movies=[]
    movie_count = 0     
    if keyword:
            movies= Movie.objects.filter(Q(title__icontains=keyword))#(Q(description__icontains=keyword) |  Q(product_name__icontains=keyword))
            movie_count =movies.count()
    else:
         movies=Movie.objects.all()
    context = {
        'movies':movies,
        'movie_count':movie_count,
    }
    
    return render(request, 'search/search_results.html',context)
