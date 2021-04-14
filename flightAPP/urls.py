from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

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
    path('flight/search/', views.find_flights),
    path('flight/reserve', views.save_reservation),
    # token
    # path('api-token/', obtain_auth_token, name='api_auth_token'),
]
