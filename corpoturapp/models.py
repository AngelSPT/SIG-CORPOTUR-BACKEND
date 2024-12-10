from django.db import models

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    
class States(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Establishments(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    direction = models.TextField()
    link_google_maps = models.URLField()

class Events(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_id = models.IntegerField()
    birth_date = models.DateField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=50)
    
    