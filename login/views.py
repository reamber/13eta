from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms
import logging
import time
import datetime
from match_site.models import user, role

# Create your views here.

#class LoginView(generic.TemplateView):
#    template_name = 'login/login.html'

logger = logging.getLogger(__name__)

def getToken(request):
    users = user.objects.all();
    if request.method == "POST":
        response = HttpResponseRedirect('/')
        #set cookie with google id that expires in 7 days
        seven_days = 60*60*24*7
        response.set_cookie('user_google_id',
                            str(request.POST['idtoken']),
                            seven_days, 
                            datetime.datetime.strftime(
                                datetime.datetime.utcnow() + \
                                datetime.timedelta(seconds=seven_days),
                                "%a, %d-%b-%Y %H:%M:%S GMT")
        )
        for u in users:
            if u.user_google_id == request.POST['idtoken']:
                return response
        new_user = user(user_name=request.POST['name'],
                        user_logged_in=True,
                        user_email=request.POST['email'],
                        user_role=role.objects.get(role='user'),
                        user_google_id=request.POST['idtoken'])
        new_user.save()
        print('new user added: ' + str(new_user))
        return response
    return HttpResponseRedirect('/')
