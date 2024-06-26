from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

from .models import  Category, Movie, Review

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Review)
