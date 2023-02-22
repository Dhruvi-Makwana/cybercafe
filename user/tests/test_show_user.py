from django.test import TestCase
from django.urls import reverse
from user.models import User, System, ConfigureSystems


class UserListingTset(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))

    def test_user_listing(self):
        userlist = self.client.get(reverse('user:showuser'), follow=True)
        self.assertTrue(userlist, 200)


