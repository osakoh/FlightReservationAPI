from rest_framework import serializers
from flightAPP.models import Flight, Passenger, Reservation
import re


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate_flight_number(self, flight_no):
        """
        format: validate_fieldName
        checks if the flight number inputted is alpha-numeric
        """
        if re.match("^[a-zA-Z0-9-]*$", flight_no) is None:
            raise serializers.ValidationError("Invalid Flight Number! Make sure it is alpha-numeric")
        return flight_no


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
