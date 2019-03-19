from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms

from match_site.models import MatchSelection
from user_profile.models import profile
from django.contrib.auth.models import User

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
    
def CreateMatch(request):
    #get post data from forma
    try:
        MatchSelection.objects.get(
            user_one=request.user,
            user_two=User.objects.get(id=request.POST['matchID'])
        )
        return HttpResponse("Match already exists")
    except:
        new_match = MatchSelection(
            user_one=request.user,
            user_two=User.objects.get(id=request.POST['matchID'])
        )
        new_match.save()
        return HttpResponse("Match created")
