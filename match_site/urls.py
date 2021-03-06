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

app_name="match"

urlpatterns = [
    path('showprofiles', views.ShowPotentialMatchesView, name="Show Potential Match Profiles"),
    path('showmatches', views.UserMatches, name="Show User Matches"),
    path('showpending', views.UserPendingMatches, name="Show User Matches"),
    path('creatematch', views.CreateMatch, name="Create New Match"),
    path('removematch', views.Unmatch, name="Unmatch"),
    
    path('', views.MatchView, name="match" ),
]
