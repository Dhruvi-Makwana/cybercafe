from django.test import TestCase
from django.urls import reverse
from user.models import User, System, ConfigureSystems
from user.choice import KB, MB, TB, GB,AVAILABLE,OCCUPIED


class SystemAssignListing(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))

    def test_system_user_list(self):
        self.create_user = User.objects.create(first_name="shivani", last_name="shah",password="1234", email="shivani@gmail.com", mobile_number= 2345343433)

        system_list = self.client.get(reverse('user:system_userlist', kwargs={'pk': self.create_user.id}), follow=True)
        self.assertTrue(system_list, 200)