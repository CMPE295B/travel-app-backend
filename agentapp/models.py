from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode
from django.utils.formats import get_format

class TravelPackage (models.Model):
    #DATE_FORMAT = '%m%d%Y'
    VACATION = 'VC'
    HONEYMOON = 'HM'
    EDUCATIONAL = 'ED'
    ADVENTURE = 'AD'
    FAMILY = 'FM'
    PILGRIMAGE ='PL'
    CREATED = 'created'
    RESERVED = 'reserved'
    INCOMPLETE = 'incomplete'
    PUBLISHED = 'published'
    PACKAGE_TYPES = (
        (VACATION, 'Vacation'),
        (HONEYMOON, 'Honeymoon'),
        (EDUCATIONAL, 'Educational'),
        (ADVENTURE, 'Adventure'),
        (FAMILY, 'Family'),
        (PILGRIMAGE, 'Pilgrimage'),
    )
    PACKAGE_STATUS = (
        (CREATED, 'created'),
        (RESERVED, 'reserved'),
        (INCOMPLETE, 'imcomplete'),
        (PUBLISHED, 'published'),
    )
    package_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    package_type = models.CharField(max_length=2,
                                    choices=PACKAGE_TYPES,
                                    default=VACATION)
    flight = models.BooleanField()
    hotel = models.BooleanField()
    insurance = models.BooleanField()
    restaurant = models.BooleanField()
    local_booking = models.BooleanField()
    status = models.CharField(max_length=10,
                                    choices=PACKAGE_STATUS,
                                    default=CREATED)
    owner = models.ForeignKey('auth.User', related_name='packages')
    
    def __unicode__(self):
        return smart_unicode(self.package_name)


class CreatedPackage (models.Model):
    pid = models.ForeignKey(TravelPackage)
    uid = models.ForeignKey('auth.User', related_name='createdpackages')
    package_name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.package_name)
    

class AssignedPackage (models.Model):
    pid = models.ForeignKey(TravelPackage)
    agentid = models.ForeignKey('auth.User', related_name='assignner')
    guideid = models.ForeignKey('auth.User', related_name='assignee')
    package_name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.package_name)


class PublishedPackage (models.Model):
    pid = models.ForeignKey(TravelPackage)
    uid = models.ForeignKey('auth.User', related_name='publishedpackages')
    package_name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self):
        return smart_unicode(self.package_name)
