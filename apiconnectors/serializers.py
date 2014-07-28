from django.contrib.auth.models import User
from .models import HotelBooking
from rest_framework import serializers



class HotelReservationSerializer(serializers.ModelSerializer):
    agentId = serializers.Field('owner.id')
    class Meta:
        model = HotelBooking
        fields = ('hotelId', 'arrivalDate','departureDate','supplierType',
                  'roomTypeCode','rateCode','chargeableRate',
                  'room1','room1FirstName','room1LastName','room1BedTypeId',
                  'room1SmokingPreference','email','firstName',
                  'lastName','city','stateProvinceCode',
                  'countryCode','postalCode','packageId','agentId')
