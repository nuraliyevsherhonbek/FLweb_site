from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    subject = forms.CharField(max_length=500)

    class Meta:
        model = Application
        fields = ('first_name', 'last_name', 'phone_number', 'subject')