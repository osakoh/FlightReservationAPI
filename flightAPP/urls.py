from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# DefaultRouter object
router = DefaultRouter()
# register viewsets
router.register('flights', views.FlightViewSet)
router.register('passengers', views.PassengerViewSet)
router.register('reservations', views.ReservationViewSet)

urlpatterns = [
    # add router url to urlpatterns
    path('', include(router.urls)),
]
