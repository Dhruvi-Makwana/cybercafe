from django.test import TestCase
from django.urls import reverse
from user.models import User
from user.models import System, ConfigureSystems
from user.choice import KB, MB, TB, GB, AVAILABLE, OCCUPIED


class UpdateSystemTest(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))

    def test_update_system(self):
        self.configure_sys = ConfigureSystems.objects.create(name="Inspire", company="DELL", ram=12, unit=KB)
        self.system = System.objects.create(name=self.configure_sys, status=AVAILABLE)
        update_sys = self.client.post(reverse('user:homepage', kwargs={'operation': 'update'}),
                                      data={'id':self.system.id, 'name__name':
                                            "core i4", 'name__company': "DELL",  'name__ram': 6, 'name__unit': 'MB',
                                            'status': 'OCCUPIED'})
        self.assertTrue(update_sys.status_code, 200)
