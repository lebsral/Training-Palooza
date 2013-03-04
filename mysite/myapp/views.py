from myapp.models import TrainingScheduled, TrainingDesired
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.forms import ScheduledForm, WantedForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm




def planned(request):
    now = datetime.now()
    events = TrainingScheduled.objects.filter(date_class_starts__gte=now.date()).order_by('date_class_starts')
    context = {
        'events': events,
    }
    return render_to_response(
        'myapp/future.html',
        context,
        context_instance=RequestContext(request),
    )


def needed(request):
    events = TrainingDesired.objects.filter(visible=True).order_by('-creation_date')
    context = {
        'events': events,
    }
    return render_to_response(
        'myapp/needed.html',
        context,
        context_instance=RequestContext(request),
    )


@login_required
def create_planned(request):
    form = ScheduledForm(request.POST or None)
    if form.is_valid():
        x = form.save(commit=False)
        x.creator = request.user
        x.save()
        messages.add_message(request, messages.SUCCESS, 'Your event was posted.  Events are listed in chronological order, so yours may not be at the top.')
        if 'next' in request.POST:
            next = request.POST['next']
        else:
            next = reverse('what_is_planned')
        return HttpResponseRedirect(next)
    return render_to_response(
        'myapp/create_planned.html',
        {'form': form},
        context_instance=RequestContext(request),
    )


@login_required
def create_needed(request):
    form = WantedForm(request.POST or None)
    if form.is_valid():
        x = form.save(commit=False)
        x.creator = request.user
        x.save()
        messages.add_message(request, messages.SUCCESS, 'Your need was posted.')
        if 'next' in request.POST:
            next = request.POST['next']
        else:
            next = reverse('what_is_needed')
        return HttpResponseRedirect(next)
    return render_to_response(
        'myapp/create_needed.html',
        {'form': form},
        context_instance=RequestContext(request),
    )


def planned_archive(request):
    now = datetime.now()
    events = TrainingScheduled.objects.filter(date_class_starts__lt=now.date()).order_by('date_class_starts')
    context = {
        'events': events,
    }
    return render_to_response(
        'myapp/archive_of_past_plans.html',
        context,
        context_instance=RequestContext(request),
    )


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            next = reverse('login')
            return HttpResponseRedirect(next)
    else:
        form = UserCreationForm()
    return render_to_response(
        'registration/register.html',
        {'form': form,},
        context_instance=RequestContext(request),
    )

