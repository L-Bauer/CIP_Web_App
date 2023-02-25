from django import forms

class NewDeptForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a new department.")
