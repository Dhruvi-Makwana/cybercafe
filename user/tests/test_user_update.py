from django.test import TestCase
from django.urls import reverse
from user.models import User
from user.models import System, ConfigureSystems


class UserUpdateTest(TestCase):
    def setUp(self):
        self.user = self.client.force_login(User.objects.create_superuser(username="sam@gmail.com", password='1234',
                                                                          email="sam@gmail.com"))

    def test_user_update(self):
        create_user = User.objects.create(first_name="shivani", last_name= "shah", password= "1234", email="shivani@gmail.com",mobile_number=2345343433)
        response = self.client.post(reverse('user:user_update',kwargs={'pk': create_user.id}), data={'first_name':'shiv','last_name':'shah','email':'shiv@gmail.com'})
        self.assertEqual(response.status_code, 302)
