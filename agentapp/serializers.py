from agentapp.models import TravelPackage, CreatedPackage, AssignedPackage, PublishedPackage
from django.contrib.auth.models import User
from rest_framework import serializers



class TravelPackageSerializer(serializers.ModelSerializer):
    ownerid = serializers.Field('owner.id')
    class Meta:
        model = TravelPackage
        fields = ('id', 'package_name','description','start_date',
                  'end_date','package_type','flight','hotel',
                  'insurance','restaurant','local_booking','status', 'ownerid')
        

class CreatedPackageSerializer(serializers.ModelSerializer):
    createrId = serializers.Field('uid.id')
    class Meta:
        model = CreatedPackage
        fields = ('id', 'package_name','pid','createrId')


class AssignedPackageSerializer(serializers.ModelSerializer):
    agentId = serializers.Field('agentid.id')
    guideId = serializers.Field('guideid.id')
    class Meta:
        model = AssignedPackage
        fields = ('id', 'package_name','pid','agentId','guideId')
   
        
class PublishedPackageSerializer(serializers.ModelSerializer):
    publisherId = serializers.Field('uid.id')
    class Meta:
        model = PublishedPackage
        fields = ('id', 'package_name','pid','publisherId')
