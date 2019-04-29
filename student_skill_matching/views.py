from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import logout 
from django.urls import reverse
from django.views import generic
from django import forms
import logging
import time
import datetime
from user_profile.models import profile, InterestTag
from match_site.models import MatchSelection
# Create your views here.

def HomeView(request):
    return render(request, "home.html")

def SearchResultsView(request):
    template_name = ''
    if(request.user.is_authenticated):
        template_name = 'searchresults.html'
    else:
        template_name = 'not_logged_in.html'
        return render(request, template_name)

    match_list=profile.objects.all()  
    search_results = []
    profile_list=list(profile.objects.exclude(profile_user=request.user).exclude(profile_perm_view=False).exclude(profile_perm_search=False))
    query=request.GET['search'].lower()
    print(query)

    for i in range(len(profile_list)):
        i_profile=profile_list[i]
        name=i_profile.profile_user.get_full_name().lower()
        tags=[x.tag_name.lower() for x in InterestTag.objects.filter(tag_user=i_profile.profile_user)]
        print(tags)
        if query in name:
            search_results.append(i_profile)    
        elif query in tags:
            search_results.append(i_profile)
        elif query in i_profile.profile_major.lower():
            search_results.append(i_profile)

    matches = []
    for s in search_results:
        if MatchSelection.objects.filter(user_two=request.user, user_one=s.profile_user).exists() and MatchSelection.objects.filter(user_one=request.user, user_two=s.profile_user).exists():
            matches.append([s, "match"])
        elif MatchSelection.objects.filter(user_one=request.user, user_two=s.profile_user).exists():
            matches.append([s, "pending"])
        else:
            matches.append([s, "none"])
    
    context={
            "search_results":matches
            }
    print(context)
    return render(request, template_name, context)
