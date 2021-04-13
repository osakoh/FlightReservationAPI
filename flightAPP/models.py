from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Flight(models.Model):  # parent model of Passenger and Reservaton
    flight_number = models.CharField(max_length=15)
    operating_airline = models.CharField(max_length=25)
    departure_city = models.CharField(max_length=25)
    arrival_city = models.CharField(max_length=25)
    date_of_departure = models.DateField()
    estimated_time_of_departure = models.TimeField()

    def __str__(self):
        return f"Flight Number: {self.flight_number}"


class Passenger(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f"{self.first_name}. {self.middle_name[0]} .{self.last_name}"


class Reservation(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='flights')
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE, related_name='passenger')

    def __str__(self):
        return f"Flight Number:{self.flight.flight_number} - " \
               f"Name: {self.passenger.first_name}.{self.passenger.middle_name[0]}.{self.passenger.last_name} "


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, *args, **kwargs):
    """
    sender: is the User model
    instance: is the user objected that created
    created: boolean value(True/False)
    creates a Token automatically when a user is created in the DB
    """
    if created:
        print(f"sender: {sender}\ninstance: {instance}\ncreated: {created}")
        Token.objects.create(user=instance)
