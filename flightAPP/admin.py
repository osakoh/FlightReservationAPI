from django.contrib import admin
from .models import Flight, Passenger, Reservation


class PassengerInline(admin.TabularInline):
    model = Passenger


class ReservationInline(admin.TabularInline):
    model = Reservation


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'middle_name', 'email', 'phone']
    list_display_links = ['first_name', 'last_name', 'middle_name', 'email', 'phone']
    inlines = [ReservationInline]


@admin.register(Reservation)
class Reservation(admin.ModelAdmin):
    list_display = ['flight', 'passenger']
    list_display_links = ['flight', 'passenger']


@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'operating_airline',
                    'departure_city', 'arrival_city',
                    'date_of_departure', 'estimated_time_of_departure']

    list_display_links = ['flight_number', 'operating_airline',
                          'departure_city', 'arrival_city',
                          'date_of_departure', 'estimated_time_of_departure']

    inlines = [ReservationInline]
