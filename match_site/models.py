from django.db import models
from django.utils import timezone

class role(models.Model):
    role = models.CharField(max_length=20)
    role_id = models.IntegerField()
    def __str__(self):
        return self.role

class user(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_logged_in = models.BooleanField(default=False)
    user_join_date = models.DateTimeField(default=timezone.now)
    user_role = models.ForeignKey(role, on_delete=models.CASCADE)
    user_google_id = models.CharField(max_length=1000)
	#possibly add field to access profile
    def __str__(self):
        return self.user_name


