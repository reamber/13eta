from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pictures')
    profile_background_image = models.ImageField(upload_to='profile_backgrounds')
    profile_bio = models.CharField(max_length=200)
    profile_education = models.CharField(max_length=100)
    profile_interests = models.CharField(max_length=100)
    profile_contact_info = models.CharField(max_length=100)
    #ADD MODEL FOR TAGS TO RELATE USERS
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.profile_user.first_name + "'s Profile"
