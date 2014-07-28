from django.conf.urls import patterns, include, url
from agentapp import agent_views
from apiconnectors import hotel_API, hotels_views
from userprofile import user_profile_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       #url(r^api/$, agentapp_agent_views.apiList.as_view()), #show api version list
                       #url(r^api/(?P<pk>[0-9]+)/$, agentapp_agent_views.apiDetail.as_view(), name='api-detail'), #show api version list
                       url(r'^users/$', user_profile_views.UserList.as_view()),
                       url(r'^users/(?P<pk>[0-9]+)/$', user_profile_views.UserDetail.as_view(), name='user-detail'),
                       url(r'^groups/$', user_profile_views.GroupList.as_view()),
                       url(r'^groups/(?P<pk>[0-9]+)/$', user_profile_views.GroupDetail.as_view(), name='group-detail'),
                       url(r'^packages/$', agent_views.PackageList.as_view()),
                       url(r'^packages/(?P<pk>[0-9]+)/$', agent_views.PackageDetail.as_view(), name='newpackage-detail'),
                       url(r'^created-packages/$', agent_views.CreatedPackageList.as_view()),
                       url(r'^created-packages/(?P<pk>[0-9]+)/$', agent_views.CreatedPackageDetail.as_view(), name='createdpackage-detail'),
                       url(r'^assigned-packages/$', agent_views.AssignedPackageList.as_view()),
                       url(r'^assigned-packages/(?P<pk>[0-9]+)/$', agent_views.AssignedPackageDetail.as_view(), name='assignedpackage-detail'),
                       url(r'^published-packages/$', agent_views.PublishedPackageList.as_view()),
                       url(r'^published-packages/(?P<pk>[0-9]+)/$', agent_views.PublishedPackageDetail.as_view(), name='publishedpackage-detail'),
                       url(r'^hotels/$', hotels_views.HotelList.as_view(), name='hotel-list'),
                       url(r'^hotel-reservation/$', hotels_views.HotelReservation.as_view(), name='hotel-reservation'),
                       url(r'^user-profile/', include('userprofile.urls')),
                       )
urlpatterns = format_suffix_patterns(urlpatterns)

