from django import forms
from .models import Profile
from django.contrib.auth.models import User
#Forms:

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (('college','year'),'branch','mobile')
