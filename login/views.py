from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib.auth import logout 
from django.urls import reverse
from django.views import generic
from django import forms
import logging
import time
import datetime

# Create your views here.
def signout(request):
    logout(request)
    return HttpResponseRedirect('/')
