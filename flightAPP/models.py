from django.db import models


class Flight(models.Model):  # parent model of Passenger and Reservaton
    flightNumber = models.CharField(max_length=15)
    operatingAirlines = models.CharField(max_length=25)
    departureCity = models.CharField(max_length=25)
    arrivalCity = models.CharField(max_length=25)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

    def __str__(self):
        return f"Flight Number:{self.flightNumber}"


class Passenger(models.Model):
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    middleName = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.firstName}. {self.middleName[0]} .{self.lastName}"


class Reservation(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name='flight')
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE, related_name='passenger')

    def __str__(self):
        return f"Flight Number:{self.flight.flightNumber} - Name: {self.passenger.firstName}.{self.passenger.middleName[0]}.{self.passenger.lastName} "
