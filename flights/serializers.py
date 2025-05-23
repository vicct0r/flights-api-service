from rest_framework import serializers
from .models import Flight, Gate, Passenger

class FlightSerializers(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = ['flight_number', 'origem', 'destino', 'data_hora_partida', 'status', 'status_display', 'gate']

    def get_status_display(self, obj):
        return obj.get_status_display()


class GateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = ['code', 'available']


class PassengerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Passenger
        fields = ['name', 'cpf', 'status_checkin', 'flight']
    

class PassengerReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'name', 'status_checkin', 'flight']


class FlightsReportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Flight
        fields = ['id', 'flight_number', 'status']

 