from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import Profile
from .forms import *
from django.http import HttpResponse

# Create your views here.
def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'Login Successful!')
                return HttpResponse('Login Successful!')
            else:
                messages.error(request,'Disabled Account! Contact admins for more info.')
        else:
            messages.error(request,"Invalid Credentials")
    else:
        form = LoginForm()
    return render(request,'registration/login.html',{'form':form})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        profile_form = ProfileRegistrationForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            #First Save the user form and then commit changes to the Profile Form due to OneToOneField
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            #Now commit changes to the profile_form
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            return redirect('login')
        else: 
            #The Forms are not valid, print errors
            messages.error(request,user_form.errors)
            messages.error(request,profile_form.errors)
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileRegistrationForm()
    return render(request,'registration/register.html',{'user_form':user_form,'profile_form':profile_form})

def user_profile(request, pk):
    profile = get_object_or_404(Profile,pk=pk)
    return render(request,'userprofile/profile.html',{'profile':profile})

def profile_edit(request, pk):
    #profile = get_object_or_404(Profile, pk=pk)
    if request.method == 'POST':
        user_form = UserEditForm(request.POST)
        profile_form = ProfileRegistrationForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = User()
            profile = Profile()
            cdu = user_form.cleaned_data
            cdp = profile_form.cleaned_data
        else:
            messages.error(request,user_form.errors)
            messages.error(request,profile_form.errors)
    else:
        user_form = UserEditForm()
        profile_form = ProfileRegistrationForm()
    return render(request,'userprofile/edit.html',{'user_form':user_form,'profile_form':profile_form})