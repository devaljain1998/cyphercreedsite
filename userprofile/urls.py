from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

#URLS:
urlpatterns = [
    # path('login/',auth_views.LoginView.as_view(),name='login'),
    # path('logout/',auth_views.LogoutViewView.as_view(),name='logout'),
    # path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

    #There are more URLS but all of this can be included with a single command:
    path('',include('django.contrib.auth.urls')),

    #path('login/',views.LoginView,name='login')
    path('register/', views.register, name='register'),
    #path('edit/', views.edit, name='edit'),
    #Activity
]