from django.db import models

# Create your models here.
class user(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_join_date = models.DateTimeField('join date')
    user_role = models.ForeignKey(roles, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_name

class roles(models.Model):
    role = models.CharField(max_length=20)
    role_id = models.IntegerField()
    def __str__(self):
        return self.role
