from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from user_profile.models import profile, InterestTag

def GetProfileView(request):
    model = profile
    template_name = 'user_profile/profile.html'
    username = None
    if request.user.is_authenticated:
        current_user = request.user
        username = request.user.username
        try:
            current_profile = profile.objects.get(profile_user=current_user)
            if(InterestTag.objects.filter(tag_user=current_user).exists()):
                interests = list(InterestTag.objects.filter(tag_user=current_user))
            else:
                interests = []
            context = {
                    'name'  :   current_user.get_full_name(),
                    'img'   :   current_profile.profile_pic,
                    'bimg'  :   current_profile.profile_background_image,
                    'bio'   :   current_profile.profile_bio,
                    'major' :   current_profile.profile_year,
                    'year'  :   current_profile.profile_major,
                    'intr'  :   interests,
                    'phone'  :   current_profile.profile_phone,
                    'email'  :   current_profile.profile_email,
            }
            return render(request, template_name, context)
        except Exception as e:
            return render(request, 'user_profile/signup.html')

    else:
        return render(request, 'not_logged_in.html')

def SignupView(request):
    template_name = 'user_profile/signup.html'
    return render(request, template_name)

def NotSignedInView(request):
    template_name = 'not_logged_in.html'
    return render(request, template_name)

def GetNewProfileView(request):
    if request.method == 'POST':
        new_profile = profile(
            profile_pic=request.FILES['profile_pic'],
            profile_background_image=request.FILES['profile_background'],
            profile_bio=request.POST['profile_bio'],
            profile_year=request.POST['profile_year'],
            profile_major=request.POST['profile_major'],
            profile_email=request.user.email,
            profile_phone=request.POST['profile_phone'],
            profile_user=request.user
        )
        new_profile.save()
        return HttpResponseRedirect('/')
    else:
        return HttpResponseForbidden("Form Error")

def EditProfileView(request):
    template_name = 'user_profile/edit.html'
    if request.user.is_authenticated:
        current_user = request.user
        try:
            current_profile = profile.objects.get(profile_user=current_user)
            if(InterestTag.objects.filter(tag_user=current_user).exists()):
                interests = ', '.join(x.tag_name for x in list(InterestTag.objects.filter(tag_user=current_user)))
            else:
                interests = ''
            context = {
                    'name'  :   current_user.get_full_name(),
                    'img'   :   current_profile.profile_pic,
                    'bimg'  :   current_profile.profile_background_image,
                    'bio'   :   current_profile.profile_bio,
                    'major' :   current_profile.profile_major,
                    'year'  :   current_profile.profile_year,
                    'intr'  :   interests,
                    'email'  :   current_profile.profile_email,
                    'phone'  :   current_profile.profile_phone,
            }
            return render(request, template_name, context)
        except Exception as e:
            return render(request, 'user_profile/signup.html')

def SaveProfileEditsView(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_profile = profile.objects.get(profile_user=request.user)
            if(request.FILES.getlist('profile_pic')):
                user_profile.profile_pic=request.FILES['profile_pic']
            if(request.FILES.getlist('profile_background')):
                user_profile.profile_background_image=request.FILES['profile_background']
            user_profile.profile_bio=request.POST['profile_bio']
            user_profile.profile_major=request.POST['profile_major']
            user_profile.profile_year=request.POST['profile_year']
            user_profile.profile_phone=request.POST['profile_phone']
            user_profile.profile_email=request.POST['profile_email']
            user_profile.save()
            prev_tags = InterestTag.objects.filter(tag_user=request.user)
            new_tags = []
            for interest in request.POST['profile_interests'].split(','):
                interest = interest.strip()
                if not prev_tags.filter(tag_user=request.user, tag_name__iexact=interest).exists():
                    new_tags.append(InterestTag(tag_user=request.user, tag_name=interest.upper()))
                else:
                    prev_tags = prev_tags.exclude(tag_user=request.user, tag_name__iexact=interest)
            for ptag in prev_tags:
                ptag.delete()
            for ntag in new_tags:
                ntag.save()
            return HttpResponseRedirect('/profile')
        else:
            return HttpResponseForbidden("Form Error")
    return HttpResponseRedirect('/profile')

def SettingsView(request):
    if request.user.is_authenticated:
        prof = profile.objects.filter(profile_user=request.user)[0]
        context={
            "see_phone":prof.profile_perm_phone,
            "notification":prof.profile_perm_notify,
            "search_prof":prof.profile_perm_search,
            "see_prof":prof.profile_perm_view,
        }
        return render(request, 'user_profile/settings.html', context)
    else:
        return render(request, 'not_logged_in.html')

def SaveSettingsView(request):
    if request.user.is_authenticated:
        prof = profile.objects.filter(profile_user=request.user)[0]
        print(request.POST)
        prof.profile_perm_phone=("phone" in request.POST.keys())
        prof.profile_perm_notify=("notify" in request.POST.keys()) 
        prof.profile_perm_search=("search" in request.POST.keys())
        prof.profile_perm_view=("view" in request.POST.keys())
        prof.save()
        return HttpResponseRedirect('/profile/settings')
    else:
        return render(request, 'not_logged_in.html')
