from django.conf.urls import patterns, include, url


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),
    (r'', include('django.contrib.auth.urls')),
    (r'^events/', include('myapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'', include('social_auth.urls')),
    (r'^accounts/logout/$', 'django.contrib.auth.views.login', {'template_name': 'myapp/login.html'}),
    url(r'^.*', 'myapp.views.needed'),
)
