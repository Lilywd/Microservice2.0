from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetup(APITestCase):
    def setUp(self):
        self.check_admin = reverse('is-admin')
        self.check_staff = reverse('is-staff')
        self.delete_user = reverse('delete-user')
        self.add_admin = reverse('add-admin')
        self.remove_admin = reverse('remove-admin')
        self.add_staff = reverse('add-staff')
        self.remove_staff = reverse('remove-staff')
        self.update_profile = reverse('update_profile')
        self.register = "/api/v1/users/"
        self.login = "/api/v1/jwt/create/"
        self.user_data = {
            'email' : "email@gmail.com",
            "first_name": "user1",
            "last_name": "test",
            "password": "letsConfirm"
        }
        self.user_data2 = {
            'email' : "email2@gmail.com",
            "first_name": "user2",
            "last_name": "test",
            "password": "letsConfirm"
        }
        self.user_data3 = {
            'email' : "email3@gmail.com",
            "first_name": "user3",
            "last_name": "test",
            "password": "letsConfirm"
        }
        return super().setUp()


    def tearDown(self):
        return super().tearDown()