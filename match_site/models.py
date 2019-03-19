from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

class MatchSelection(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name="first_matcher")
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name="second_matcher")
    def __str__(self):
        return self.user_one.get_full_name() + ", " + self.user_two.get_full_name()
