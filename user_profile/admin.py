from django.contrib import admin

from user_profile.models import profile, InterestTag

# Register your models here.
admin.site.register(profile)
admin.site.register(InterestTag)

