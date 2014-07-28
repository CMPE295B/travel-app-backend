from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from agentapp.models import TravelPackage
# Create your models here.

class HotelBooking(models.Model):
    NON_SMOKING='NS'
    SMOKING='S'
    EITHER='E'
    hotelId =  models.IntegerField(max_length=10)
    arrivalDate =  models.CharField(max_length=10)
    departureDate =  models.CharField(max_length=10)
    supplierType =  models.CharField(max_length=1)
    rateKey =  models.CharField(max_length=50)
    roomTypeCode = models.IntegerField(max_length=7)
    rateCode = models.IntegerField(max_length=7)
    chargeableRate = models.FloatField()
    room1 = models.IntegerField(max_length=1)
    room1FirstName = models.CharField(max_length=30)
    room1LastName = models.CharField(max_length=30)
    room1BedTypeId = models.IntegerField(max_length=2)
    SMOKING_PREFERENCE = (
        (NON_SMOKING, 'NS'),
        (SMOKING, 'S'),
        (EITHER, 'E'),
    )
    room1SmokingPreference = models.CharField(max_length=12,
                                    choices=SMOKING_PREFERENCE,
                                    default=NON_SMOKING)
    email = models.EmailField()
    firstName = models.CharField(max_length=30, default="test")
    lastName = models.CharField(max_length=30, default="tester")
    # homephone - address1 fields are default values needed for testing purpose
    homePhone = models.IntegerField(max_length=10, default= 2145370159)
    workPhone = models.IntegerField(max_length=10, default= 2145370159)
    creditCardType = models.CharField(max_length=2, default ="CA")
    creditCardNumber = models.IntegerField(max_length=16, default= 5401999999999999)
    creditCardIdentifier = models.IntegerField(max_length=3, default= 123)
    creditCardExpirationMonth = models.IntegerField(max_length=2, default= 11)
    creditCardExpirationYear= models.IntegerField(max_length=4, default= 2016)
    address1 =  models.CharField(max_length=30, default ="travelnow")
    city = models.CharField(max_length=30)
    stateProvinceCode = models.CharField(max_length=2)
    countryCode = models.CharField(max_length=20, default="US")
    postalCode = models.IntegerField(max_length=5)
    # UC = unconfirmed, CF = confirmed, CX = cancelled, PS = pending, ER = error, DT=deleted
    bookingStatus = models.CharField(max_length=2, default ="UC")
    packageId = models.ForeignKey(TravelPackage, related_name='travel_package')
    itineraryId = models.IntegerField(max_length=12, default=0)
    owner = models.ForeignKey('auth.User', related_name='booking_agent')
    
    def __unicode__(self):
        return smart_unicode(self.email)
