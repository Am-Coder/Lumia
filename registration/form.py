from django import forms
from registration.models import User
# from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput()
        }
        fields = ['username', 'password', 'first_name', 'last_name', 'email', 'birth_date', 'bio']


class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

