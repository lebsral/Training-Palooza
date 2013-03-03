from django.contrib import admin
from myapp.models import TrainingDesired, TrainingScheduled, Location

admin.site.register(TrainingDesired)
admin.site.register(TrainingScheduled)
admin.site.register(Location)
