from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms
from django.db.models import Q

from match_site.models import MatchSelection
from user_profile.models import profile
from django.contrib.auth.models import User

def MatchView(request):
    template_name = 'match_site/match.html'
    return render(request, template_name)

# Displays a list of all the user profiles
def ShowAllProfilesView(request):
    template_name = 'match_site/profile_list.html'
    profile_list=list(profile.objects.exclude(profile_user=request.user))  
    match_list=MatchSelection.objects.filter(
            Q(user_one=request.user)|Q(user_two=request.user)
    )
    
    for i in range(len(profile_list)):
        profile_list[i] = [
                profile_list[i], 
                len(list(match_list.filter(user_one=profile_list[i].profile_user)))!=0,
                len(list(match_list.filter(user_two=profile_list[i].profile_user)))!=0,
        ]

    context={
            "profile_list":profile_list
    }
    return render(request, template_name, context)
    
def CreateMatch(request):
    #get post data from form
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
        
def Unmatch(request):
    try:
        MatchSelection.objects.get(
            user_one=request.user,
            user_two=User.objects.get(id=request.POST['matchID'])
        ).delete()
        return HttpResponse("Match removed")
    except:
        return HttpResponse("Failed to remove match")

def UserMatches(request):
    template_name = 'match_site/user_match_list.html'
    matches = list(MatchSelection.objects.filter(user_one=request.user))
    confirmed_matches = []
    for m in matches:
        if MatchSelection.objects.filter(user_one=m.user_two, user_two=request.user).exists():
            confirmed_matches.append(m)
    context = {
        "match_list": confirmed_matches,
    }
    return render(request, template_name, context)


def UserPendingMatches(request):
    template_name = 'match_site/user_pending_match_list.html'
    try:
        context = {
            "match_list": list(MatchSelection.objects.filter(user_one=request.user)),
        }
    except:
        context = {
            "match_list": None
        }
    return render(request, template_name, context)

def ShowAllMatchesView(request):
    template_name = 'match_site/match_list.html'
    match_list=profile.objects.all()  
    context={
            "match_list":match_list
    }
    return render(request, template_name, context)
