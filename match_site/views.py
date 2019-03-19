from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms


# Create your views here.

class HomeView(generic.TemplateView):
    template_name = 'match_site/index.html'

