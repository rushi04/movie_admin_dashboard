from django.db import models

# Create your models here.

class Login(models.Model):
    username : models.CharField(max_length=30,primary_key=True)
    password : models.CharField(max_length = 10)


class Movie(models.Model):
    movie_name :models.CharField(max_length=30,primary_key=True)
    movie_descreption : models.CharField(max_length=100)
    movie_director :models.CharField(max_length=30)
    movie_price:models.IntegerField(max_length=10)
    movie_total_tickets:models.IntegerField(max_length=10)
    movie_start_time:models.DateTimeField(auto_now_add=True)
    movie_end_time:models.DateTimeField(auto_now_add=True)