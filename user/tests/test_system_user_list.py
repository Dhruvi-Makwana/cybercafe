from django.test import TestCase
from django.urls import reverse
from user.models import User, System, ConfigureSystems
from user.choice import KB, MB, TB, GB,AVAILABLE,OCCUPIED


class SystemAssignListing(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))

    def test_system_user_list(self):
        # self.configure_sys =
        self.system = System.objects.create(name=ConfigureSystems.objects.create(name="DELL Inspire", company="DELL", ram=6, unit=KB), status=AVAILABLE)
        system_list = self.client.get(reverse('user:system_userlist',kwargs={'pk':self.system.id}), follow=True)
        self.assertTrue(system_list, 200)
