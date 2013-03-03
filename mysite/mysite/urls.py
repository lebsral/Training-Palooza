from django.conf.urls import patterns, include, url
from myapp.api import KnightResource  # for the api, need to make one of these for each one
from myapp.views import hello_view
knight_resource = KnightResource()  # for the api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),


    # this is for the api from tastypie
    # this tastypie example is based on http://blog.brabadu.com/2011/06/easy-rest-api-with-django-tastypie.html
    # ./api/knight/list/?format=json should return something
# the username and api key will of course be different each time
# base-lebsral.dotcloud.com/api/knight/list/?format=json&username=admin&api_key=5f3f44c63c559374db033dc3446c53ca6b200724

    url(r'^api/', include(knight_resource.urls)),

    url(r'^$', view=hello_view, name='hello_page'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
