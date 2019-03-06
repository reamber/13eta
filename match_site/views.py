from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms

from user_profile.models import profile

def MatchView(request):
    template_name = 'match_site/match.html'
    return render(request, template_name)

# Displays a list of all the user profiles
def ShowAllProfilesView(request):
    template_name = 'match_site/profile_list.html'
    profile_list=profile.objects.all()  
    context={
            "profile_list":profile_list
    }
    return render(request, template_name, context)
