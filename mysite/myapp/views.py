from myapp.models import TrainingScheduled, TrainingDesired
from django.shortcuts import render_to_response
from django.template import RequestContext
from myapp.forms import ScheduledForm, WantedForm, UserChangerForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def planned(request):
    now = datetime.now()
    events = TrainingScheduled.objects.filter(date_class_starts__gte=now.date()).order_by('date_class_starts')
   # messages.add_message(request, messages.SUCCESS, RANDOM_TIP)
   # Random_Tip = 4
    messages.add_message(request, messages.SUCCESS, "Tip: Doing a new employee training?  Invite outsiders. They gain insight into your organization at no cost to you.")
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
   # messages.add_message(request, messages.SUCCESS, "Tip: Doing a new employee training?  Invite outsiders. They gain insight into your organization at no cost to you.")
    context = {
        'events': events,
    }
    return render_to_response(
        'myapp/needed.html',
        context,
        context_instance=RequestContext(request),
    )


def create_planned(request):
    if request.user.is_authenticated():
        z = 1
    else:
        msgtxt = 'You are not logged in.  Which is fine.  You can still post.  But, you will not be able to easily delete or edit your posts later.  ' + '<a href="' + reverse('login') + '">Log in</a>' + ' | ' + '<a href="' + reverse('new_user_register') + '">New Account</a>'
        messages.add_message(request, messages.SUCCESS,  msgtxt, extra_tags='safe')
    form = ScheduledForm(request.POST or None)
    if form.is_valid():
        x = form.save(commit=False)
        if request.user.is_authenticated():
            x.creator = request.user
        else:
            x.creator = User.objects.get(username__exact='anonymous')
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


def create_needed(request):
    if request.user.is_authenticated():
        z = 1
    else:
        msgtxt = 'You are not logged in.  Which is fine.  You can still post.  But, you will not be able to easily delete or edit your posts later.  ' + '<a href="' + reverse('login') + '">Log in</a>' + ' | ' + '<a href="' + reverse('new_user_register') + '">New Account</a>'
        messages.add_message(request, messages.SUCCESS,  msgtxt, extra_tags='safe')
    form = WantedForm(request.POST or None)
    if form.is_valid():
        x = form.save(commit=False)
        if request.user.is_authenticated():
            x.creator = request.user
        else:
            x.creator = User.objects.get(username__exact='anonymous')
        x.save()
        messages.add_message(request, messages.SUCCESS, 'Your training need was posted.')
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
        {'form': form, },
        context_instance=RequestContext(request),
    )


@login_required
def changeuser(request):
    form = UserChangerForm(request.POST or None)
    if form.is_valid():
        x = form.save(commit=False)
        if request.user.is_authenticated():
            x.creator = User.objects.get
            x.save()
            messages.add_message(request, messages.SUCCESS, 'Your user information was saved.')
        else:
            messages.add_message(request, messages.SUCCESS, 'Your user information was not saved.')
        if 'next' in request.POST:
            next = request.POST['next']
        else:
            next = reverse('what_is_needed')
        return HttpResponseRedirect(next)
    return render_to_response(
        'registration/changeuser.html',
        {'form': form},
        context_instance=RequestContext(request),
    )

