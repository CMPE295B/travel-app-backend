from django.conf.urls import patterns, include, url
from userprofile import user_profile_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
                       url(r'^', user_profile_views.UserProfileList.as_view()),
                       url(r'^(?P<pk>[0-9]+)/$', user_profile_views.UserProfileDetail.as_view(),
                       name='profile-detail'),
                       )
