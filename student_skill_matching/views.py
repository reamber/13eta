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

# Create your views here.

def HomeView(request):
    return render(request, "home.html")

def SearchResultsView(request):
    template_name = ''
    if(request.user.is_authenticated):
        template_name = 'searchresults.html'
    else:
        template_name = 'not_logged_in.html'
        return render(request, template_name, context)

    match_list=profile.objects.all()  
    search_results = []
    profile_list=list(profile.objects.all())
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

    context={
            "search_results":search_results
            }
    print( context)
    return render(request, template_name, context)
