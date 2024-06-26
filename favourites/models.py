from django.db import models

from accounts.models import CustomUser
from movies.models import Movie

# Create your models here.

class Favourite(models.Model):
    user= models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user','movie')