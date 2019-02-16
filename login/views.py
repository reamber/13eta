from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms

from match_site.models import user

# Create your views here.

class LoginView(generic.TemplateView):
    template_name = 'login/login.html'

