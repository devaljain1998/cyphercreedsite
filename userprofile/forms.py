from django import forms
from .models import Profile
from django.contrib.auth.models import User
#Forms:

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('college','year','branch','description','mobile','github_url','linkedin_url')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class UserEdit(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

