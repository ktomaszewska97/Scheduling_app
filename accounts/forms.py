from django import forms
from django.contrib.auth.models import User


class TeamCreateForm(forms.Form):
    name = forms.CharField(required=True)
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
