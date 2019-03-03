from django.test import TestCase
import datetime

from django.test import TestCase
from django.contrib.auth import get_user, get_user_model
from django.test import Client

from user_profile.models import profile

class ProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='temporary')
        self.user.set_password('temporary')
        self.user.save()
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
    def tearDown(self):
        self.user.delete()

