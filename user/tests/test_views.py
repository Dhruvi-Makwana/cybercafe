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

    def test_assign_system(self):
        user = User.objects.create(username="heta", first_name="heta", email="heta@gmail.com",
                                                    mobile_number=3434343433)
        configure_sys = ConfigureSystems.objects.create(name="DELL Inspire", company="DELL", ram=6, unit=KB)
        system = System.objects.create(name=configure_sys, status=AVAILABLE)
        get_assign_data = self.client.post(reverse('user:homepage', kwargs={'operation': 'assign'}),
                                           data={'system_user': user.id, 'system': system.id},
                                           content_type='application/json')
        self.assertEqual(get_assign_data, 200)
        self.assertJSONEqual(get_assign_data, {'status': 'success'})

    # def test_release_system(self):
    #
    #     self.configure_sys = ConfigureSystems.objects.create(name="DELL Inspire", company="DELL", ram=6, unit=KB)
    #     self.system = System.objects.create(name=self.configure_sys, status=OCCUPIED)
    #     release_responce = self.client.post(reverse('user:homepage', kwargs={'operation': 'release'}),
    #                                         data={'system': self.system.id})
    #     self.assertEqual(release_responce.status_code, 200)
