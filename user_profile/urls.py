"""student_skill_matching URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name='user_profile'

urlpatterns = [
    path('signup', views.SignupView, name="User Signup"),
    path('notsignedin', views.NotSignedInView, name="User Sign In"),
    path('getNewProfile', views.GetNewProfileView, name="Get new profile"),
    path('editprofile', views.EditProfileView, name="Edit profile"),
    path('saveprofile', views.SaveProfileEditsView, name="Save edited profile"),
    path('settings', views.SettingsView, name="Settings"),
    path('savesettings', views.SaveSettingsView, name="Save Settings"),
    path('', views.GetProfileView, name="User Profile"),
]
