# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.urls import reverse

from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150,unique=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def get_url(self):
        return reverse('category_list',args=[self.slug])

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    is_available= models.BooleanField(default=True)
    
    def __str__(self):
        return self.title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return f"{self.user.username}'s review of {self.movie.title}"
