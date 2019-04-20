from django.test import TestCase
import datetime

from django.test import TestCase
from django.contrib.auth import get_user, get_user_model
from django.test import Client
from django.contrib.auth.models import User
from django.template import RequestContext
from django.template.loader import render_to_string

from user_profile.models import profile
from match_site.models import MatchSelection

class MatchTests(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='temporary',first_name="TestFirstName", last_name="TestLastName")
        self.profuser = User.objects.create_user(username='profile',first_name="TestFirstName", last_name="TestLastName")

        self.test_profile = profile(profile_pic="1",profile_background_image="2",profile_bio="3",profile_education="4",profile_interests="5",profile_contact_info="6",profile_user=self.profuser)
        self.test_prof2 = profile(profile_user=self.user)

        self.test_profile.save()
        self.test_prof2.save()

        self.user.set_password('temporary')
        self.profuser.set_password('temporary')
        self.user.save()
        self.profuser.save()

    def test_matches_page_no_matches(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/match/showmatches').content.decode('utf8')
        self.assertIn("You have no confirmed matches right now, go look for some new matches!", str(response))

    def test_pendingmatches_page_no_matches(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/match/showpending').content.decode('utf8')
        self.assertIn("You have no pending matches right now, go look for some new matches!", str(response))

    def test_new_match(self):
        self.client.login(username="profile",password="temporary")
        



    def tearDown(self):
        self.user.delete()
        self.profuser.delete()
