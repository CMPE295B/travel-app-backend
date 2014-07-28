from django.contrib.auth.models import User, Group
from rest_framework import serializers
from userprofile.models import UserProfile


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user','phone','company_name','address',
                  'city','state','zipcode','country','website')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','id', 'username','first_name','last_name','email','password','groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')