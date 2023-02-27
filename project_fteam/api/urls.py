from django.urls import path, include
from rest_framework import routers
from .views import (GamesViewSet, DevelopersViewSet ,PublishersViewSet,
                    PlayerViewSet, GenresViewSet, SalesViewSet,
                    add_money, spend_money)

router = routers.DefaultRouter()
router.register(r'Games', GamesViewSet, basename="Games")
router.register(r'Developers', DevelopersViewSet, basename="Developers")
router.register(r'Publishers', PublishersViewSet, basename="Publishers")
router.register(r'Players', PlayerViewSet, basename="Player")
router.register(r'Genres', GenresViewSet, basename="Genres")
router.register(r'Sales', SalesViewSet, basename="Sales")



urlpatterns = [
    path('', include(router.urls)),
    path('add_money/<str:pk>', add_money, name="add-money"),
    path('spend_money/<str:pk>', spend_money, name="spend-money"),
]