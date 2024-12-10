from rest_framework import serializers
from .models import Recipes, Events, Entrepreuners, Establishments, People, Programs, Users, Types, events_establishments, programs_entrepreuners, people_users, events_users

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = ('id','name','description','ingredients','instructions', 'image')

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id','name','description','date','link_google_maps')

class EntrepreunersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrepreuners
        fields = ('id','name','id_people')

class EstablishmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establishments
        fields = ('id','name','description','direction','link_google_maps')

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('id','first_name','last_name','document_id','birth_date','phone','gender')

class ProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Programs
        fields = ('id','name','description','start_date','end_date')    

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','name','email','password','id_type')

class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Types
        fields = ('id','name','description')    
    
class events_establishmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = events_establishments
        fields = ('id','id_event','id_establishment')   

class programs_entrepreunersSerializer(serializers.ModelSerializer):
    class Meta:
        model = programs_entrepreuners
        fields = ('id','id_program','id_entrepreuner')  
    
class people_usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = people_users
        fields = ('id','id_user','id_people')   

class events_usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = events_users
        fields = ('id','id_event','id_user')


