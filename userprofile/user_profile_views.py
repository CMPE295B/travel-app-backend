from django.contrib.auth.models import User, Group
from rest_framework import generics
from userprofile.serializers import UserProfileSerializer, UserSerializer, GroupSerializer
from userprofile.models import UserProfile

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (IsAdminUser,)
    paginate_by = 2
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserProfileList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    #permission_classes = (IsAdminUser,)
    paginate_by = 2
    
class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = (IsAdminUser,)
    paginate_by = 2
    
class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer 