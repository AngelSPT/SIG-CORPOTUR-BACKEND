from .models import Recipes, Events, Entrepreuners, Establishments, People, Programs, Users, Types, events_establishments, programs_entrepreuners, people_users, events_users
from rest_framework import viewsets, permissions
from .serializers import RecipesSerializer, TypesSerializer, UsersSerializer, EventsSerializer, EntrepreunersSerializer, EstablishmentsSerializer, PeopleSerializer, ProgramsSerializer, events_establishmentsSerializer, programs_entrepreunersSerializer, people_usersSerializer, events_usersSerializer

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    permission_classes = [permissions.AllowAny]

class TypesViewSet(viewsets.ModelViewSet):
    queryset = Types.objects.all()
    serializer_class = TypesSerializer
    permission_classes = [permissions.AllowAny]

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [permissions.AllowAny]

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    permission_classes = [permissions.AllowAny]

class EntrepreunersViewSet(viewsets.ModelViewSet):
    queryset = Entrepreuners.objects.all()
    serializer_class = EntrepreunersSerializer
    permission_classes = [permissions.AllowAny]

class EstablishmentsViewSet(viewsets.ModelViewSet):
    queryset = Establishments.objects.all()
    serializer_class = EstablishmentsSerializer
    permission_classes = [permissions.AllowAny]

class PeopleViewSet(viewsets.ModelViewSet):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = [permissions.AllowAny]

class ProgramsViewSet(viewsets.ModelViewSet):
    queryset = Programs.objects.all()
    serializer_class = ProgramsSerializer
    permission_classes = [permissions.AllowAny]

class events_establishmentsViewSet(viewsets.ModelViewSet):
    queryset = events_establishments.objects.all()
    serializer_class = events_establishmentsSerializer
    permission_classes = [permissions.AllowAny]

class programs_entrepreunersViewSet(viewsets.ModelViewSet):
    queryset = programs_entrepreuners.objects.all()
    serializer_class = programs_entrepreunersSerializer
    permission_classes = [permissions.AllowAny]

class people_usersViewSet(viewsets.ModelViewSet):
    queryset = people_users.objects.all()
    serializer_class = people_usersSerializer
    permission_classes = [permissions.AllowAny]

class events_usersViewSet(viewsets.ModelViewSet):
    queryset = events_users.objects.all()
    serializer_class = events_usersSerializer
    permission_classes = [permissions.AllowAny]



