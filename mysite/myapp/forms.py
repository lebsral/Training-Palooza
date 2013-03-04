from django import forms
from myapp.models import TrainingScheduled, TrainingDesired
from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper


class ScheduledForm(forms.ModelForm):
    description = forms.CharField(max_length=500, widget=forms.Textarea)
    contact_email = forms.EmailField(max_length=150, required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'ScheduledForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Create Event'))
        super(ScheduledForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TrainingScheduled
        fields = ('title', 'date_class_starts', 'where', 'description', 'fullfills',
            'audience', 'cost', 'person', 'contact_email', 'contact_phone', 'location',)


class WantedForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)
    contact_email = forms.EmailField(max_length=254, required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'WantedForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit Need'))
        super(WantedForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TrainingDesired
        fields = ('title', 'organization', 'description', 'fullfills',
            'audience', 'cost', 'person', 'contact_email', 'contact_phone', 'location',)