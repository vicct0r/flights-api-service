from django.shortcuts import render
from rest_framework import generics

from datetime import date, datetime, time
from django.utils.timezone import now, make_aware

from .serializers import FlightsReportSerializer

from .serializers import FlightSerializers, GateSerializers, PassengerSerializers, PassengerReportSerializer
from .models import Flight, Gate, Passenger

class FlightListCreateView(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers


class FlightRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers


class GateListCreateView(generics.ListCreateAPIView):
    queryset = Gate.objects.all()
    serializer_class = GateSerializers


class GateRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gate.objects.all()
    serializer_class = GateSerializers


class PassengerListCreateView(generics.ListCreateAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers


class PagessengerRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers


class FlightReportAPIView(generics.ListAPIView):
    serializer_class = FlightsReportSerializer

    def get_queryset(self):
        time_now = now()
        end_day = make_aware(datetime.combine(time_now.date(), time.max))

        return Flight.objects.filter(data_hora_partida__range=(time_now, end_day))


class PassengerRerpotAPIView(generics.ListCreateAPIView):
    serializer_class = PassengerSerializers
    queryset = Passenger.objects.all()

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('flight_pk'):
            return self.get_queryset.filter(flight_id=self.kwargs.get('flight_id'))
        return self.queryset.all()


class GateReportAPIView(generics.ListCreateAPIView):
    serializer_class = Gate
    queryset = Gate.objects.all()

    def get_queryset(self, *args, **kwargs):
        if self.kwargs.get('gate_pk'):
            return self.get_queryset.filter(gate_id=self.kwargs.get('flight_id'))
        return self.queryset.all()
