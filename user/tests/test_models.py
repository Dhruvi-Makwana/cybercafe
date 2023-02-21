from django.test import TestCase
from user.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="samantha",first_name="samanatha", last_name="prabhu", email="sam@gmail.com")

    def test_first_name_label(self):
        user = User.objects.get(first_name="samanatha")
        field_label = user._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_username_label(self):
        user = User.objects.get(first_name="samanatha")
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_user_email(self):
        user = User.objects.values('username').get(first_name="samanatha")
        self.assertTrue(user,'sam@gmail.com')
