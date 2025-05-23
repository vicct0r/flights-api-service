from django.shortcuts import render
from rest_framework import generics

from datetime import date, datetime, time
from django.utils.timezone import now, make_aware

from .serializers import FlightsReportSerializer

from .serializers import FlightSerializers, GateSerializers, PassengerSerializers, PassengerReportSerializer
from .models import Flight, Gate, Passenger

from .permissions import StaffReadOnlySuperuserFullAcess


class FlightListCreateView(generics.ListCreateAPIView):
    permission_classes = [StaffReadOnlySuperuserFullAcess]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers


class FlightRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [StaffReadOnlySuperuserFullAcess]
    queryset = Flight.objects.all()
    serializer_class = FlightSerializers


class GateListCreateView(generics.ListCreateAPIView):
    permission_classes = [StaffReadOnlySuperuserFullAcess]
    queryset = Gate.objects.all()
    serializer_class = GateSerializers


class GateRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [StaffReadOnlySuperuserFullAcess]
    queryset = Gate.objects.all()
    serializer_class = GateSerializers


class PassengerListCreateView(generics.ListCreateAPIView):
    permission_classes = [StaffReadOnlySuperuserFullAcess]
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers


class PagessengerRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [StaffReadOnlySuperuserFullAcess]
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializers


class FlightReportAPIView(generics.ListAPIView):
    permission_classes = [StaffReadOnlySuperuserFullAcess]
    serializer_class = FlightsReportSerializer

    def get_queryset(self):
        time_now = now()
        end_day = make_aware(datetime.combine(time_now.date(), time.max))

        return Flight.objects.filter(

            data_hora_partida__range=(time_now, end_day),
        )


class PassengerRerpotAPIView(generics.ListCreateAPIView):
    serializer_class = PassengerSerializers
    queryset = Passenger.objects.all()

    def get_queryset(self, *args, **kwargs):
        flight_id = self.kwargs['pk']
        return Passenger.objects.filter(flight_id=flight_id)


class GateReportAPIView(generics.ListCreateAPIView):
    serializer_class = GateSerializers
    queryset = Gate.objects.all()

    def get_queryset(self, *args, **kwargs):
        flight_id = self.kwargs.get('pk')
        return Gate.objects.filter(flight=flight_id)