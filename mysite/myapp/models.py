from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db.models.query import QuerySet



def today():
    now = datetime.now()
    start = datetime.min.replace(year=now.year, month=now.month,
        day=now.day)
    end = (start + timedelta(days=1)) - timedelta.resolution
    return (start, end)


class EventQuerySet(QuerySet):
    def today(self):
        return self.filter(date_class_starts__range=today())


class EventManager(models.Manager):
    def get_query_set(self):
        return EventQuerySet(self.model)

    def today(self):
        return self.get_query_set().today()


class Location(models.Model):
    city = models.CharField(verbose_name="City of Training", max_length=100)
    state = models.CharField(verbose_name="State of Training", max_length=30)
    country = models.CharField(verbose_name="Country of Training", max_length=100, default="United States of America")

    def __unicode__(self):
        return "%s, %s" % (self.city, self.state)


class TrainingDesired(models.Model):
    creator = models.ForeignKey(User)
    title = models.CharField(verbose_name="Title of the training", max_length=200)
    organization = models.CharField(verbose_name="Organization needing", max_length=200, blank=True, null=True)
    creation_date = models.DateTimeField(default=datetime.now)
    description = models.CharField(verbose_name="About this training", max_length=500)
    fullfills = models.CharField(verbose_name="Requirements it will fullfill", max_length=200, blank=True, null=True)
    audience = models.CharField(verbose_name='Who this is for', max_length=200, blank=True, null=True)
    person = models.CharField(verbose_name="Person to contact", max_length=50)
    contact_email = models.EmailField(verbose_name="Contact email", max_length=254, blank=True, null=True)
    contact_phone = models.CharField(verbose_name="Contact phone", max_length=40, blank=True, null=True)
    cost = models.CharField(verbose_name="Thoughts about cost", max_length=200, blank=True, null=True,)
    location = models.ForeignKey(Location)
    visible = models.BooleanField(default=True)

    def __unicode__(self):
        return "%s needed by %s" % (self.title, self.organization)

    class Meta(object):
        verbose_name_plural = 'Trainings Desired'


class TrainingScheduled(models.Model):
    creator = models.ForeignKey(User)
    date_class_starts = models.DateField(verbose_name="Date training starts")
    where = models.CharField(verbose_name="Where training will be held", max_length=150, blank=True, null=True)
    title = models.CharField(verbose_name="Title of the training", max_length=200)
    creation_date = models.DateTimeField(default=datetime.now)
    description = models.CharField(verbose_name="About this training", max_length=500)
    fullfills = models.CharField(verbose_name="Requirements it will fullfill", max_length=200, blank=True, null=True)
    audience = models.CharField(verbose_name='Who this is for', max_length=200, blank=True, null=True)
    person = models.CharField(verbose_name="Person to contact", max_length=50)
    contact_email = models.EmailField(verbose_name="Contact email", max_length=254, blank=True, null=True)
    contact_phone = models.CharField(verbose_name="Contact phone", max_length=40, blank=True, null=True)
    cost = models.CharField(verbose_name="Thoughts about cost", max_length=200, blank=True, null=True,)
    location = models.ForeignKey(Location)
    visible = models.BooleanField(default=True)

    objects = EventManager()

    def __unicode__(self):
        return "%s at %s on %s" % (self.title, self.where, self.date_class_starts)

    class Meta(object):
        verbose_name_plural = 'Trainings Scheduled'
