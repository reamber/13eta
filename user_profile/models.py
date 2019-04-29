from django.db import models

from django.contrib.auth.models import User
from match_site.models import MatchSelection

# Create your models here.
class profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pictures')
    profile_background_image = models.ImageField(upload_to='profile_backgrounds')
    profile_bio = models.CharField(max_length=200)
    profile_year = models.CharField(max_length=100,default="")
    profile_major = models.CharField(max_length=100, default="")
    profile_phone = models.CharField(max_length=100, default="")
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_email = models.CharField(max_length=100, default="no email provided")
    profile_perm_phone = models.BooleanField(default="False")
    profile_perm_notify = models.BooleanField(default="False")
    profile_perm_search = models.BooleanField(default="True")
    profile_perm_view = models.BooleanField(default="True")

    def __str__(self):
        return self.profile_user.first_name + "'s Profile"
    def get_interests(self):
        return InterestTag.objects.filter(tag_user=self.profile_user)

class InterestTag(models.Model):
    tag_name = models.CharField(max_length=100)
    tag_active = models.BooleanField(default=True)
    tag_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.tag_name+"<" + self.tag_user.get_full_name() + ">"

