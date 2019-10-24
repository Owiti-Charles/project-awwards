from django.test import TestCase
from .models import *


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='charles', password='wer2345uyq')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def tearDown(self):
        self.user.delete()

