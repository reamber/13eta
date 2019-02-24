from django.shortcuts import render
from django.views import generic

# Create your views here.
from student_profile.models import profile

class ProfileView(generic.DetailView):
    model = profile
    template_name = 'profile.html'
    '''
    if "user_google_id" in request.COOKIES:
        return HttpResponse('User Profile')
    else:
        return HttpResponseRedirect('/login')
        '''
