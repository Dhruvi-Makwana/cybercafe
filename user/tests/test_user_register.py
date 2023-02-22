from django.test import TestCase
from django.urls import reverse
from user.models import User
from user.models import System, ConfigureSystems


class UserRegisterTest(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))

    def test_user_register(self):
        self.user_register = self.client.post(reverse('user:user_register'), data={'first_name': "shivani",
                                                                                'last_name':"shah", 'password': "1234",
                                                                                   'email': "shivani@gmail.com",
                                                                                   'mobile_number': 2345343433})

        self.assertEqual(self.user_register.status_code, 302)
