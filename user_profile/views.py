from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from user_profile.models import profile
from match_site.models import user

def getProfile(request):
    model = profile
    template_name = 'user_profile/profile.html'
    username = None
    if request.user.is_authenticated:
        current_user = request.user
        username = request.user.username
        try:
            current_profile = profile.objects.get(profile_user=current_user)
            context = {
                    'name'  :   current_user.first_name + ' ' + current_user.last_name,
                    'img'   :   current_profile.profile_pic,
                    'bimg' :   current_profile.profile_background_image,
                    'bio'   :   current_profile.profile_bio,
                    'edu'   :   current_profile.profile_education,
                    'intr'  :   current_profile.profile_interests,
                    'cont'  :   current_profile.profile_contact_info,
            }
            return render(request, template_name, context)
        except Exception as e:
            print("No profile exists yet for this user!")
            print(e)
            return render(request, 'user_profile/signup.html')
            
    else:
        return HttpResponse('Not signed in')

def signup(request):
    template_name = 'user_profile/signup.html'
    return render(request, template_name)

