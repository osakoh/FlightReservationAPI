from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Flight, Passenger, Reservation
from .serializers import FlightSerializer, PassengerSerializer, ReservationSerializer


@api_view(['POST'])
def find_flights(request):
    """
    request.data: contains the data received from DRF
    :returns: queryset of flights matching the departure_city, arrival_city, and date_of_departure in the request
    """
    # contains=case-insensitive; gte=greater than or equal to
    flights = Flight.objects.filter(departure_city__contains=request.data['departure_city'],
                                    arrival_city__icontains=request.data['arrival_city'],
                                    date_of_departure__gte=request.data['date_of_departure'])
    serializer = FlightSerializer(flights, many=True)  # serializer object
    return Response(serializer.data)


@api_view(['POST'])
def save_reservation(request):
    # print(request.data['flight'])
    flight = Flight.objects.get(id=request.data['flight'])

    # create passenger object
    passenger = Passenger.objects.create(first_name=request.data['first_name'],
                                         last_name=request.data['last_name'],
                                         middle_name=request.data['middle_name'],
                                         email=request.data['email'],
                                         phone=request.data['phone'])

    reservation = Reservation.objects.create(flight=flight, passenger=passenger)

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


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
