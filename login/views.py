from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms
import logging
import time

from match_site.models import user, role

# Create your views here.

#class LoginView(generic.TemplateView):
#    template_name = 'login/login.html'

logger = logging.getLogger(__name__)

def getToken(request):
    users = user.objects.all();
    print(request)
    if request.method == "POST":
        for u in users:
            if u.user_google_id == request.POST['idtoken']:
                logger.debug('returning user')
                u.user_logged_in=True
                return HttpResponseRedirect('/') 

        new_user = user(user_name=request.POST['name'],
                        user_logged_in=True,
                        user_email=request.POST['email'],
                        user_role=role.objects.get(role='user'),
                        user_google_id=request.POST['idtoken'])
        new_user.save()
        logger.debug('new user added: ' + str(new_user))
    return HttpResponseRedirect('/')
