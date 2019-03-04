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
                    'name'  :   current_user.get_full_name(),
                    'img'   :   current_profile.profile_pic,
                    'bimg'  :   current_profile.profile_background_image,
                    'bio'   :   current_profile.profile_bio,
                    'edu'   :   current_profile.profile_education,
                    'intr'  :   current_profile.profile_interests,
                    'cont'  :   current_profile.profile_contact_info,
            }
            return render(request, template_name, context)
        except Exception as e:
            return render(request, 'user_profile/signup.html')
            
    else:
        return render(request, 'user_profile/profile_login.html') 

def signup(request):
    template_name = 'user_profile/signup.html'
    return render(request, template_name)

def notsignedin(request):
    template_name = 'user_profile/profile_login.html'
    return render(request, template_name)

def getNewProfile(request):
   print('getNewProfile view called')
   #model = profile
   #NEED TO ADD SOME KIND OF ID???
   new_profile = profile(
        profile_pic=request.POST['profile_pic'],
        profile_background_image=request.POST['profile_background'],
        profile_bio=request.POST['profile_bio'],
        profile_education=request.POST['profile_education'],
        profile_interests=request.POST['profile_interests'],
        profile_contact_info=request.POST['profile_contact_info'],
        profile_user=request.user
    )
   new_profile.save()
   print('new profile added: ' + str(new_profile))
   return HttpResponseRedirect('/')
