from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from user_profile.models import profile
from match_site.models import user

def getProfile(request):
    model = profile
    template_name = 'user_profile/profile.html'
    if "user_google_id" in request.COOKIES:
        current_user = user.objects.get(user_google_id=request.COOKIES['user_google_id'])
        current_profile = profile.objects.get(profile_user=current_user)
        context = {
                'name'  :   current_user.user_name,
                'img'   :   current_profile.profile_pic,
                'b_img' :   current_profile.profile_background_image,
                'bio'   :   current_profile.profile_bio,
                'edu'   :   current_profile.profile_education,
                'intr'  :   current_profile.profile_interests,
                'cont'  :   current_profile.profile_contact_info,
        }
        return render(request, template_name, context)
    else:
        return HttpResponse('Not signed in')

def signup(request):
    template_name = 'user_profile/signup.html'
    return render(request, template_name)

