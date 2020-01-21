from django import forms
from registration.models import User
# from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class SignInForm(forms.Form):
    pass
