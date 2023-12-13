from rest_framework import serializers
from tickets.models import Reservation,Guest,Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta :
        model=Movie
        fields= '__all_'
class ReservationSerializer(serializers.ModelSerializer):
    class Meta :
        model=Reservation
        fields= '__all_'
class GuestSerializer(serializers.ModelSerializer):
    class Meta :
        model=Guest
        fields= ['pk','reservation','name','mobile']
