from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from myapp import views


urlpatterns = patterns('',
    url(r'^create_planned/$', views.create_planned, name='create_planned'),
    url(r'^create_needed/$', views.create_needed, name='create_needed'),
    url(r'^planned/$', views.planned, name="what_is_planned"),
    url(r'^needed/$', views.needed, name="what_is_needed"),
    url(r'^planned_archive/$', views.planned_archive, name="what_was_offered"),
    url(r'^register/$', views.register, name="new_user_register"),
    url(r'^accounts/logout/$', logout, name="user_logout"),
    url(r'^myapp/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^myapp/changeprofile/$', views.changeuser, name="change_profile"),
    url(r'^myapp/mypostsneeded/$', views.mypostsneeded, name="see_mypost_needed"),
    url(r'^myapp/mypostsscheduled/$', views.mypostsscheduled, name="see_mypost_scheduled"),
)
