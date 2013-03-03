#from django.contrib.auth.models import User
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

from myapp.models import Knight


class KnightResource(ModelResource):
    class Meta:
        queryset = Knight.objects.all()
        resource_name = 'knight/list'
        excludes = ['id']
        include_resource_uri = False
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
# need to make this per user?  but how???  now returns all objects even those not created by the user
   # class Meta:
   # queryset = User.objects.all()

