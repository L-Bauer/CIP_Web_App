import datetime

from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class NewDeptForm(forms.Form):
    completed_date = forms.DateField(help_text="Enter the completed date.")

    def clean_renewal_date(self):
        data = self.cleaned_data['completed_date']

        # Check if a date is not in the past.
        if data > datetime.date.today():
            raise ValidationError(_('Completed date is in the future'))

        # Remember to always return the cleaned data.
        return data