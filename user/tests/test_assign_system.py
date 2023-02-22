from django.test import TestCase
from django.urls import reverse
from user.models import User
from user.models import System, ConfigureSystems
from user.choice import KB, MB, TB, GB, AVAILABLE, OCCUPIED
from datetime import datetime


class AssignSystemTest(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))

    def test_assign_system(self):
        get_assign_data = self.client.post(reverse('user:homepage', kwargs={'operation': 'assign'}),
                                            data={'users':
                                            User.objects.create(username="heta", first_name="heta", email="heta@gmail.com",mobile_number=3434343433).id,
                                            'systems':
                                            System.objects.create(name=ConfigureSystems.objects.create(name="DELL Inspire", company="DELL", ram=6, unit=KB), status=AVAILABLE).id,
                                            'start_time': datetime.now()},
                                       content_type='application/json')
        self.assertEqual(get_assign_data, 200)
        self.assertJSONEqual(get_assign_data, {'status': 'success'})
