from rest_framework import routers
from django.urls import path, include
from .api import RecipesViewSet

router = routers.DefaultRouter()

router.register('api/recipes', RecipesViewSet)

urlpatterns = router.urls