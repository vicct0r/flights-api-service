from django.contrib import admin
from .models import Flight, Passenger, Gate

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ['flight_number', 'origem', 'destino', 'data_hora_partida', 'status', 'gate']
    search_fields = ['flight_number', 'origem', 'destino', 'data_hora_partida', 'status', 'gate']


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'status_checkin', 'flight', 'checkin']
    search_fields = ['name', 'cpf', 'status_checkin', 'flight', 'checkin']


@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ['code', 'available']
    search_fields = ['code', 'available']