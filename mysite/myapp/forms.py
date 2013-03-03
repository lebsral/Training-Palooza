from django import forms
from myapp.models import TrainingScheduled, TrainingDesired


class ScheduledForm(forms.ModelForm):
    description = forms.CharField(max_length=500, widget=forms.Textarea)

    class Meta:
        model = TrainingScheduled
        fields = ('title', 'date_class_starts', 'where', 'description', 'fullfills',
            'audience', 'person', 'contact_email', 'contact_phone', 'location',)


class WantedForm(forms.ModelForm):
    description = forms.CharField(max_length=500, widget=forms.Textarea)

    class Meta:
        model = TrainingDesired
        fields = ('title', 'organization', 'description', 'fullfills',
            'audience', 'person', 'contact_email', 'contact_phone', 'location',)
