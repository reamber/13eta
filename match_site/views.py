from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms


# Create your views here.

def MatchView(request):
    template_name = 'match_site/match.html'
    return render(request, template_name)
