from .models import Recipes
from rest_framework import viewsets, permissions
from .serializers import RecipesSerializer

class RecipesViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipesSerializer
    permission_classes = [permissions.AllowAny]