from django import forms
from matrivume_profile import models


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=100)


class IdentityForm(forms.ModelForm):
    birth_date = forms.CharField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = models.Identity
        exclude = ('user_profile', 'id')
