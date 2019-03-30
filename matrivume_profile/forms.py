from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=4, max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=100)
