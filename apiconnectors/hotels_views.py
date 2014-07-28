from django.shortcuts import render
from django.views.generic.base import View
from django.views import generic
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from apiconnectors.hotel_API import HotelAPI
from apiconnectors.hotel_reservation import HotelBookingAPI
from apiconnectors.models import HotelBooking
from apiconnectors.serializers import HotelReservationSerializer
from django.shortcuts import render, render_to_response, RequestContext
from agentapp.permissions import IsOwnerOrReadOnly
from apiconnectors.hotel_availability import AvailableHotel
try: import simplejson as json
except ImportError: import json

class BookingAgent(object):
    queryset = HotelBooking.objects.all()
    serializer_class = HotelReservationSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
        

class HotelList(View):
    
    def get(self, request):

        city = request.GET.get('city', False)
        state = request.GET.get('state', False)
        startDate = request.GET.get('startDate', False)
        endDate = request.GET.get('endDate', False)
        
        api = HotelAPI()
        #hotels = api.getHotelList('Fresno', 'CA', 'US', '09/12/2014', '09/15/2014', '1')
        hotels = api.getHotelList(city, state, startDate, endDate)
        #return HttpResponse(json.dumps(hotels, sort_keys = True, indent = 4, separators=(',', ': ')))
        return HttpResponse(json.dumps(hotels))

class HotelReservation(BookingAgent, APIView):
    pass


    def post(self, request):
        ahotel = AvailableHotel()
        
        rate_key = ahotel.getRateKey(request.DATA.get('hotelId', ''), request.DATA.get('room1', ''),
                                    request.DATA.get('arrivalDate', ''),request.DATA.get('departureDate', ''))
        data = {
                "hotelId": request.DATA.get('hotelId', ''),
                "arrivalDate": request.DATA.get('arrivalDate', ''),
                "departureDate": request.DATA.get('departureDate', ''),
                "supplierType": request.DATA.get('supplierType', ''),
                "rateKey": rate_key,
                "roomTypeCode": request.DATA.get('roomTypeCode', ''),
                "rateCode": request.DATA.get('rateCode', ''),
                "chargeableRate": request.DATA.get('chargeableRate', ''),
                "room1": request.DATA.get('room1', ''),
                "room1FirstName": request.DATA.get('room1FirstName', ''),
                "room1LastName": request.DATA.get('room1LastName', ''),
                "room1BedTypeId": request.DATA.get('room1BedTypeId', ''),
                "room1SmokingPreference": request.DATA.get('room1SmokingPreference', ''),
                "email": request.DATA.get('email', ''),
                "firstName": request.DATA.get('firstName', ''),
                "lastName": request.DATA.get('lastName', ''),
                "city": request.DATA.get('city', ''),
                "stateProvinceCode": request.DATA.get('stateProvinceCode', ''),
                "countryCode": request.DATA.get('countryCode', ''),
                "postalCode": request.DATA.get('postalCode', '')    
            }
        reservationRequest = HotelBookingAPI()
        reservation = reservationRequest.bookHotel(data)
        #confirmation = reservation['HotelRoomReservationResponse']['reservationStatusCode']
        #itinerary = reservation['HotelRoomReservationResponse']['itineraryId']
        #updateInfo = HotelBooking(hotelId= data['hotelId'])
        #updateInfo = HotelBooking(bookingStatus=confirmation)
        #updateInfo = HotelBooking(itineraryId=itinerary)
        #updateInfo.save()
        # return Response(request.DATA)
        return Response(json.dumps(reservation))
       
"""
class ReservationConfirmation (generics.RetrieveUpdateDestroyAPIView):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer
"""