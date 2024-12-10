from rest_framework import routers
from django.urls import path, include
from .api import RecipesViewSet, TypesViewSet, PeopleViewSet, EstablishmentsViewSet, UsersViewSet, EventsViewSet, ProgramsViewSet, EntrepreunersViewSet, events_usersViewSet, people_usersViewSet, programs_entrepreunersViewSet, events_establishmentsViewSet

router = routers.DefaultRouter()

router.register('api/recipes', RecipesViewSet)
router.register('api/types', TypesViewSet)
router.register('api/people', PeopleViewSet)
router.register('api/establishments', EstablishmentsViewSet)
router.register('api/users', UsersViewSet)
router.register('api/events', EventsViewSet)
router.register('api/programs', ProgramsViewSet)
router.register('api/entrepreuners', EntrepreunersViewSet)
router.register('api/events_users', events_usersViewSet)
router.register('api/people_users', people_usersViewSet)
router.register('api/programs_entrepreuners', programs_entrepreunersViewSet)
router.register('api/events_establishments', events_establishmentsViewSet)

urlpatterns = router.urls