from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^agentapp/', include('agentapp.urls')),
    url(r'^$', 'agentapp.agent_views.home', name='home'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    #url(r'^accounts/', include('accounts.urls')),
    )

