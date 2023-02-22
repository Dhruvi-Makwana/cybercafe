from django.test import TestCase
from django.urls import reverse
from user.models import User, System, ConfigureSystems,System_User_Histories
from user.choice import KB, MB, TB, GB, AVAILABLE, OCCUPIED
from datetime import datetime


class ReleaseSystemTest(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))

    def test_release_system(self):
        # self.configure_sys = ConfigureSystems.objects.create(name="Inspire", company="DELL", ram=12, unit=KB)
        # self.system = System.objects.create(name=self.configure_sys, status=AVAILABLE)
        # self.create_user = User.objects.create(first_name="shivani", last_name="shah",password="1234", email="shivani@gmail.com", mobile_number= 2345343433)
        create_history = System_User_Histories.objects.create(system_user=User.objects.create(first_name="shivani", last_name="shah",password="1234", email="shivani@gmail.com", mobile_number= 2345343433),
                                                              system=System.objects.create(name=ConfigureSystems.objects.create(name="Inspire", company="DELL", ram=12, unit=KB), status=AVAILABLE),
                                                              assign_time=datetime.now())
        release_responce = self.client.post(reverse('user:homepage', kwargs={'operation': 'release'}),
                                        data={'system': create_history.id})
        self.assertEqual(release_responce.status_code, 200)
