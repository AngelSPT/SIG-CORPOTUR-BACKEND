from django.db import models

# Create your models here.

class Types(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Recipes(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()

class Establishments(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    direction = models.TextField()
    link_google_maps = models.URLField()

class Events(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    date = models.DateField()
    link_google_maps = models.URLField()
    id_type = models.ForeignKey(Types, on_delete=models.CASCADE)

class Users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    id_type = models.ForeignKey(Types, on_delete=models.CASCADE)

class People(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    document_id = models.IntegerField()
    birth_date = models.DateField()
    phone = models.IntegerField()
    gender = models.CharField(max_length=50)
    
class Programs(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Entrepreuners(models.Model):
    name = models.CharField(max_length=50)
    id_people = models.ForeignKey(People, on_delete=models.CASCADE)

class people_users(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    id_people = models.ForeignKey(People, on_delete=models.CASCADE)

class programs_entrepreuners(models.Model):
    id_program = models.ForeignKey(Programs, on_delete=models.CASCADE)
    id_entrepreuner = models.ForeignKey(Entrepreuners, on_delete=models.CASCADE)

class events_establishments(models.Model):
    id_event = models.ForeignKey(Events, on_delete=models.CASCADE)
    id_establishment = models.ForeignKey(Establishments, on_delete=models.CASCADE)

class events_users(models.Model):
    id_event = models.ForeignKey(Events, on_delete=models.CASCADE)
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    