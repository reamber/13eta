from django.db import models

# Create your models here.
class role(models.Model):
    role = models.CharField(max_length=20)
    role_id = models.IntegerField()
    def __str__(self):
        return self.role
		
class profile(modelss.Model):
    profile_profile_pic = models.CharField(max_length=100)
    profile_background_image = models.CharField(max_length=100)
    profile_bio = models.CharField(max_length=200)
    profile_education = models.CharField(max_length=100)
    profile_interests = models.CharField(max_length=100)
	profile_contact_info = models.CharField(max_length=100)
    #ADD MODEL FOR TAGS TO RELATE USERS
    profile_user = models.ForeignKey(user, on_delete=models.CASCADE)
    def __str__():
	   return ""
