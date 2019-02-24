from django.db import models

from match_site.models import user

# Create your models here.
class profile(models.Model):
    profile_pic = models.CharField(max_length=100)
    profile_background_image = models.CharField(max_length=100)
    profile_bio = models.CharField(max_length=200)
    profile_education = models.CharField(max_length=100)
    profile_interests = models.CharField(max_length=100)
    profile_contact_info = models.CharField(max_length=100)
    #ADD MODEL FOR TAGS TO RELATE USERS
    profile_user = models.ForeignKey(user, on_delete=models.CASCADE)
    def __str__():
        return self.profile_bio
