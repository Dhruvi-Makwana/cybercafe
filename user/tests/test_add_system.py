from django.test import TestCase
from django.urls import reverse
from user.models import User
from user.models import System, ConfigureSystems
from user.choice import KB, MB, TB, GB,AVAILABLE,OCCUPIED

from datetime import datetime


class CreateSystemTest(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                     email="sam@gmail.com"))

    def test_create_system(self):
        self.response = self.client.post(reverse('user:homepage', kwargs={'operation': 'create'}), data={'name':
                                                "DELL Inspire", 'company': "DELL",  'ram': 6, 'unit': 'KB'})
        self.assertEqual(self.response.status_code, 200)



