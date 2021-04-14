from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

from . import views

# DefaultRouter object
router = DefaultRouter()
# swagger object
schema_view = get_swagger_view(title='Flight Reservation API')

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
    path('api-token/', obtain_auth_token, name='api_auth_token'),
    #     documentation
    path(r'docs/', schema_view),

]
