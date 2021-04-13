from django.shortcuts import render
from rest_framework import viewsets

from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer


class FlightViewSet(viewsets.ModelViewSet):
    """
    viewsets.ReadOnlyModelViewSet: exposes only the read-based operations i.e get(many) & get(single/detail)
    viewsets.ModelViewSet: handles all pk and non-pk based operations
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    """
    viewsets.ReadOnlyModelViewSet: exposes only the read-based operations i.e get(many) & get(single/detail)
    viewsets.ModelViewSet: handles all pk and non-pk based operations
    """
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    viewsets.ReadOnlyModelViewSet: exposes only the read-based operations i.e get(many) & get(single/detail)
    viewsets.ModelViewSet: handles all pk and non-pk based operations
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
