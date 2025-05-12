from django.db import models
from django.core.exceptions import ValidationError

class Gate(models.Model):
    code = models.CharField(max_length=3, unique=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class Flight(models.Model):
    PROGRAMADO = 'pro'
    EMBARQUE = 'emb'
    CONCLUIDO = 'con'

    STATUS_FLIGHT_CHOICES = (
        (PROGRAMADO, 'Programado'),
        (EMBARQUE, 'Embarque'),
        (CONCLUIDO, 'Concluído')
    )

    flight_number = models.IntegerField()
    origem = models.CharField(max_length=80)
    destino = models.CharField(max_length=80)
    data_hora_partida = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=3, choices=STATUS_FLIGHT_CHOICES)
    gate = models.OneToOneField(Gate, related_name='flight', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.flight_number} | {self.data_hora_partida}'

    def save(self, *args, **kwargs):

        if self.gate:
            self.gate.available = False
            self.gate.save()
        
        if self.status == Flight.CONCLUIDO and self.gate:
            self.gate.available = True
            self.gate.save()

            self.gate = None
        
        super().save(*args, **kwargs)


class Passenger(models.Model):
    PENDING = 'pending'
    DONE = 'done'

    STATUS_CHECKIN_CHOICES = (
        (PENDING, 'Pending'),
        (DONE, 'Done')
    )

    name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=12, unique=True)
    status_checkin = models.CharField(max_length=7, choices=STATUS_CHECKIN_CHOICES, default=PENDING)
    flight = models.ForeignKey(Flight, related_name='passenger', on_delete=models.SET_NULL, blank=True, null=True)
    checkin = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.flight.status == self.flight.CONCLUIDO:
            raise ValidationError("Check-in já não é mais permitido para este voo!")
        else:
            self.status_checkin = Passenger.DONE

        super().save(*args, **kwargs)