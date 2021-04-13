from django.contrib import admin
from .models import Flight, Passenger, Reservation


class PassengerInline(admin.TabularInline):
    model = Passenger


class ReservationInline(admin.TabularInline):
    model = Reservation


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['firstName', 'lastName', 'middleName', 'email', 'phone']
    list_display_links = ['firstName', 'lastName', 'middleName', 'email', 'phone']
    inlines = [ReservationInline]


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ['flight', 'passenger']
    list_display_links = ['flight', 'passenger']


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flightNumber', 'operatingAirlines',
                    'departureCity', 'arrivalCity',
                    'dateOfDeparture', 'estimatedTimeOfDeparture']

    list_display_links = ['flightNumber', 'operatingAirlines',
                          'departureCity', 'arrivalCity',
                          'dateOfDeparture', 'estimatedTimeOfDeparture']

    inlines = [ReservationInline]
