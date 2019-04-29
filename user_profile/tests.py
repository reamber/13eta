from django.test import TestCase
import datetime

from django.test import TestCase
from django.contrib.auth import get_user, get_user_model
from django.test import Client
from django.contrib.auth.models import User
from django.template import RequestContext
from django.template.loader import render_to_string

from user_profile.models import profile, InterestTag

class ProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(email="test@test.com",username='temporary',first_name="TestFirstName", last_name="TestLastName")
        self.profuser = User.objects.create_user(username='profile',first_name="TestFirstName", last_name="TestLastName")

        self.test_profile = profile(profile_pic="1",profile_background_image="2",profile_bio="3",profile_major="4",profile_year="4",profile_phone="6", profile_email="test@test.com",profile_user=self.profuser)

        self.test_profile.save()

        self.user.set_password('temporary')
        self.profuser.set_password('temporary')
        self.user.save()
        self.profuser.save()

        self.intTag = InterestTag(tag_name="TestInterest", tag_user=self.profuser)
        self.intTag.save()

    def test_guest_profile(self):
        response = self.client.get('/profile/')
        self.assertIn('You are not signed in', str(response.content))

    def test_user_without_profile(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/profile/')
        self.assertIn('Create Your Profile', str(response.content))

    def test_user_with_profile(self):
        self.client.login(username='temporary', password='temporary')
        test_prof = profile(profile_bio="test_profile",profile_user=self.user)
        test_prof.save()
        response = self.client.get('/profile/')
        self.assertIn('test_profile', str(response.content))
        test_prof.delete()

    def test_user_profile_template_name(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIn((User.objects.get(username="profile").get_full_name()), str(response))

    def test_user_profile_template_bio(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIn("Bio: </strong> 3", str(response))

    def test_user_profile_template_year(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIn("Year: </strong> 4", str(response))

    def test_user_profile_template_major(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIn("Major: </strong> 4", str(response))

    def test_user_profile_template_interests(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIn("TestInterest", str(response))

    def test_user_profile_template_email(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIn("Email: </strong> test@test.com", str(response))

    def test_user_profile_template_phone(self):
        self.client.login(username="profile",password="temporary")
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIn("Phone: </strong> 6", str(response))

    def test_user_profile_is_not_empty(self):
        self.client.login(username='profile', password='temporary')
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIsNot(response, " ", 'message')

    def tearDown(self):
        self.test_profile.delete()
        self.intTag.delete()
        self.user.delete()
        self.profuser.delete()
