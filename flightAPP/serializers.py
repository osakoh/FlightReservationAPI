from rest_framework import serializers
from flightAPP.models import Flight, Passenger, Reservation
import re


def is_arrival_city_valid(data):
    """
    custom validation function for 'arrival_city':
    data: contains an Ordered dictionary of the entire field data
    """
    # print("Arrival City->", data['arrival_city'])
    if len(data['arrival_city']) < 3:
        raise serializers.ValidationError("Length of Arrival City cannot be less than 3.")
    elif re.match("^[a-zA-Z]*$", data['arrival_city']) is None:
        raise serializers.ValidationError("Arrival City should only contain alphabets")
    return data


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

        # informs DRF about validators outside of this class
        validators = [is_arrival_city_valid]

    def validate_flight_number(self, flight_no):
        """
        format: validate_fieldName; the flight number is dynamically passed into this function at runtime
        checks if the flight number inputted is alpha-numeric
        """
        # print("Validate Funtionvalidate_flight_number")
        if re.match("^[a-zA-Z0-9-]*$", flight_no) is None:
            raise serializers.ValidationError("Invalid Flight Number! Make sure it is alpha-numeric.")
        return flight_no

    def validate(self, data):
        """
        :param data: contains an Ordered dictionary of the entire field data
        :return: valid data
        """
        # print("validate")
        # print(data)
        if len(data['departure_city']) < 3:
            raise serializers.ValidationError("Length of Departure City cannot be less than 3.")
        elif re.match("^[a-zA-Z]*$", data['departure_city']) is None:
            raise serializers.ValidationError("Departure City should only contain alphabets")
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
