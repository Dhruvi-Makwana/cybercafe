from django.test import TestCase
from django.urls import reverse
from user.models import User, System, ConfigureSystems


class SystemAssignListing(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))
    def test_system_assign(self):
        system_list = self.client.get(reverse('user:assign_system_listing'), follow=True)
        self.assertTrue(system_list, 200)

