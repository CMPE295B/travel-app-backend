from agentapp.models import TravelPackage, CreatedPackage, AssignedPackage, PublishedPackage
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from agentapp.serializers import TravelPackageSerializer, CreatedPackageSerializer
from agentapp.serializers import AssignedPackageSerializer, PublishedPackageSerializer
from agentapp.permissions import IsOwnerOrReadOnly
from django.shortcuts import render, render_to_response, RequestContext

class PackageOwner(object):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    
    def pre_save(self, obj):
        obj.owner = self.request.user
        
class PackageList(PackageOwner, ListCreateAPIView):
    pass

class PackageDetail(PackageOwner, RetrieveUpdateDestroyAPIView):
    pass

class CreatedPackageList(PackageOwner, ListCreateAPIView):
    queryset = CreatedPackage.objects.all()
    serializer_class = CreatedPackageSerializer

class CreatedPackageDetail(PackageOwner, RetrieveUpdateDestroyAPIView):
    queryset = CreatedPackage.objects.all()
    serializer_class = CreatedPackageSerializer

class AssignedPackageList(PackageOwner, ListCreateAPIView):
    queryset = AssignedPackage.objects.all()
    serializer_class = AssignedPackageSerializer

class AssignedPackageDetail(PackageOwner, RetrieveUpdateDestroyAPIView):
    queryset = AssignedPackage.objects.all()
    serializer_class = AssignedPackageSerializer

class PublishedPackageList(PackageOwner, ListCreateAPIView):
    queryset = PublishedPackage.objects.all()
    serializer_class = PublishedPackageSerializer

class PublishedPackageDetail(PackageOwner, RetrieveUpdateDestroyAPIView):
    queryset = PublishedPackage.objects.all()
    serializer_class = PublishedPackageSerializer

def home(request):
    return render_to_response("index.html",
                              locals(),
                              context_instance = RequestContext(request)
                             )

"""
class PackageList(generics.ListCreateAPIView):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer

class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TravelPackage.objects.all()
    serializer_class = TravelPackageSerializer
"""