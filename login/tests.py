import datetime

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user, get_user_model
from django.test import Client
from django.contrib.auth.models import User


class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.user = User.objects.create_user(username='temporary')
        self.user.set_password('temporary')
        self.user.save()
        
    def test_login(self):
        self.assertIs(self.client.login(username='temporary', password='temporary'), True)

    def test_login_fail(self):
        self.assertIs(self.client.login(username='wrong', password='wrong'), False)

    def test_matchpage_without_signin(self):
        response = self.client.get('/match/').content.decode('utf8')
        self.assertIn("Please log in", str(response))

    def test_profilepage_without_signin(self):
        response = self.client.get('/profile/').content.decode('utf8')
        self.assertIn("You are not signed in!", str(response))

    def tearDown(self):
        self.user.delete()
