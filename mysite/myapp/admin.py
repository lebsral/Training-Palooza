from django.contrib import admin
from myapp.models import Knight

admin.site.register(Knight)

# needs to be in a module that will be
# loaded before users are being created
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tastypie.models import create_api_key
post_save.connect(create_api_key, sender=User)

# the lines below just need to be in any admin in one app
# this is to show the apikey next to the user
# see tastypie docs for details

from tastypie.admin import ApiKeyInline
from tastypie.models import ApiAccess, ApiKey
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


admin.site.register(ApiKey)
admin.site.register(ApiAccess)


class UserModelAdmin(UserAdmin):
    inlines = UserAdmin.inlines + [ApiKeyInline]

admin.site.unregister(User)
admin.site.register(User, UserModelAdmin)
