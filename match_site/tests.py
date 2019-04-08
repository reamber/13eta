from django.test import TestCase
import datetime

from django.test import TestCase
from django.contrib.auth import get_user, get_user_model
from django.test import Client
from django.contrib.auth.models import User
from django.template import RequestContext
from django.template.loader import render_to_string

from user_profile.models import profile

class MatchTests(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='temporary',first_name="TestFirstName", last_name="TestLastName")
        self.profuser = User.objects.create_user(username='profile',first_name="TestFirstName", last_name="TestLastName")

        self.test_profile = profile(profile_pic="1",profile_background_image="2",profile_bio="3",profile_education="4",profile_interests="5",profile_contact_info="6",profile_user=self.profuser)
        self.test_profile.save()

        self.user.set_password('temporary')
        self.profuser.set_password('temporary')
        self.user.save()
        self.profuser.save()

    def test_pendingmatch(self):
        self.client.login(username="profile",password="temporary")

        response = self.client.get('/match/showprofiles').content.decode('utf8')

        self.assertIn((User.objects.get(username="profile").get_full_name()), str(response))

    def tearDown(self):
        self.user.delete()
        self.profuser.delete()
