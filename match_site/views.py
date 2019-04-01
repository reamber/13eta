from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms
from django.db.models import Q

from match_site.models import MatchSelection
from user_profile.models import profile, InterestTag
from django.contrib.auth.models import User

def MatchView(request):
    template_name = ''
    if(request.user.is_authenticated):
        return HttpResponseRedirect('showprofiles')
    else:
        template_name = 'not_logged_in.html'
    return render(request, template_name)

# Displays a list of all the user profiles
def ShowPotentialMatchesView(request):
    template_name = ''
    if(request.user.is_authenticated):
        template_name = 'match_site/potential_match_list.html'
    else:
        template_name = 'not_logged_in.html'
        return render(request, template_name, context)

    profile_list=list(profile.objects.exclude(profile_user=request.user))  
    match_list=MatchSelection.objects.filter(
            Q(user_one=request.user)|Q(user_two=request.user)
    )

    for i in range(len(profile_list)):
        if(InterestTag.objects.filter(tag_user=profile_list[i].profile_user).exists()):
            interests = list(InterestTag.objects.filter(tag_user=profile_list[i].profile_user))
        else:
            interests = []
        profile_list[i] = [
                profile_list[i], 
                len(list(match_list.filter(user_one=profile_list[i].profile_user)))!=0,
                len(list(match_list.filter(user_two=profile_list[i].profile_user)))!=0,
                interests,
                CalcMatchLevel(request, request.user, profile_list[i].profile_user)
        ]
    profile_list = sorted(profile_list, reverse=True, key = lambda x: x[4])

    context={
            "profile_list":profile_list
            }
    return render(request, template_name, context)

def CalcMatchLevel(request, user, potential_match):
    user_interests = set(x.tag_name for x in InterestTag.objects.filter(tag_user=request.user))
    pm_interests = set(x.tag_name for x in InterestTag.objects.filter(tag_user=potential_match))
    #Jaccard similarity
    similar = user_interests.intersection(pm_interests)
    if((len(user_interests)+len(pm_interests)-len(similar)) == 0):
        return 0
    similarity_score = float(len(similar)) / (len(user_interests)+len(pm_interests)-len(similar))
    return similarity_score

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
        if(MatchSelection.objects.filter(user_one=new_match.user_two, user_two=request.user).exists()):
            return HttpResponse("Match completed")
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
    template_name = ''
    if(request.user.is_authenticated):
        template_name = 'match_site/user_match_list.html'
    else:
        template_name = 'not_logged_in.html'

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
    template_name = ''
    if(request.user.is_authenticated):
        template_name = 'match_site/user_pending_match_list.html'   
    else:
        template_name = 'not_logged_in.html'
    matches = list(MatchSelection.objects.filter(user_one=request.user))
    confirmed_matches = []

    for m in matches:
        if MatchSelection.objects.filter(user_one=m.user_two, user_two=request.user).exists():
            confirmed_matches.append(m)
    try:
        match_list=list(set(list(MatchSelection.objects.filter(user_one=request.user))) - set(confirmed_matches))
        for i in range(len(match_list)):
            m_profile = profile.objects.get(profile_user=match_list[i].user_two)
            if(InterestTag.objects.filter(tag_user=m_profile.profile_user).exists()):
                interests = list(InterestTag.objects.filter(tag_user=m_profile.profile_user))
            else:
                interests = []
            match_list[i] = [ 
                    match_list[i], 
                    [m_profile, interests]
            ]
        context = {
            "match_list": match_list
        }
        return render(request, template_name, context)
    except Exception as e:
        print(e)
        context = {
                "match_list": None
                }
        return render(request, template_name, context)

def ShowAllMatchesView(request):
    template_name = ''
    if(request.user.is_authenticated):
        template_name = 'match_site/match_list.html'
    else:
        template_name = 'not_logged_in.html'

    match_list=profile.objects.all()  
    context={
            "match_list":match_list
            }
    return render(request, template_name, context)
