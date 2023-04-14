from .test_setup import TestSetup
from app.serializers import User
from django.shortcuts import get_object_or_404

class TestViews(TestSetup):
    def test_user_register_fail_with_no_data(self):
        res = self.client.post(self.register)
        self.assertEqual(res.status_code, 400)
    def test_user_register(self):
        res = self.client.post(self.register, self.user_data, format ="json")
        self.assertEqual(res.status_code, 201)
    def test_user_cannot_login_without_being_verified(self):
        self.client.post(self.login, self.user_data, format ="json")
        res = self.client.post(self.login, self.user_data, format ="json")
        self.assertEqual(res.status_code, 401)
    def test_user_can_login_after_being_verified(self):
        response = self.client.post(self.register, self.user_data, format ="json")
        data = response.data
        email = data['email']
        user = get_object_or_404(User, email=email)
        user.is_active = True
        user.save()
        res = self.client.post(self.login, self.user_data, format ="json")
        self.assertEqual(res.status_code, 200)

    def test_IsAdmin_for_unauthorized_user(self):
        res = self.client.get(self.check_admin)
        self.assertEqual(res.status_code, 401)
        res = self.client.get(self.check_admin)
        self.assertEqual(res.status_code, 401)
    def test_IsAdmin_for_verified_user(self):
        response1 = self.client.post(self.register, self.user_data, format ="json")
        email1 = response1.data['email']
        user1 = get_object_or_404(User, email=email1)
        user1.is_active = True
        user1.save()
        res = self.client.post(self.login, self.user_data, format ="json")
        auth_headers = {'HTTP_AUTHORIZATION': 'JWT ' + res.data["access"],}
        res2 = self.client.get(self.check_admin, **auth_headers)
        self.assertEqual(res2.status_code, 403)
    def test_IsAdmin_for_staff_user(self):
        response2 = self.client.post(self.register, self.user_data2, format ="json")
        email2 = response2.data['email']
        user2 = get_object_or_404(User, email=email2)
        user2.is_active = True
        user2.is_staff = True
        user2.is_admin = False
        user2.save()
        res = self.client.post(self.login, self.user_data2, format ="json")
        auth_headers = {'HTTP_AUTHORIZATION': 'JWT ' + res.data["access"],}
        res2 = self.client.get(self.check_admin, **auth_headers)
        self.assertEqual(res2.status_code, 403)
    def test_IsAdmin_for_admin_user(self):
        response3 = self.client.post(self.register, self.user_data3, format ="json")
        email3 = response3.data['email']
        user3 = get_object_or_404(User, email=email3)
        user3.is_active = True
        user3.is_staff = True
        user3.is_admin = True
        user3.save()
        res = self.client.post(self.login, self.user_data3, format ="json")
        auth_headers = {'HTTP_AUTHORIZATION': 'JWT ' + res.data["access"],}
        res2 = self.client.get(self.check_admin, **auth_headers)
        self.assertEqual(res2.status_code, 200)

    def test_IsStaff_for_unauthorized_user(self):
        res = self.client.get(self.check_staff)
        self.assertEqual(res.status_code, 401)
        res = self.client.get(self.check_staff)
        self.assertEqual(res.status_code, 401)
    def test_IsStaff_for_verified_user(self):
        response1 = self.client.post(self.register, self.user_data, format ="json")
        email1 = response1.data['email']
        user1 = get_object_or_404(User, email=email1)
        user1.is_active = True
        user1.is_staff = False
        user1.is_admin = False
        user1.save()
        res = self.client.post(self.login, self.user_data, format ="json")
        auth_headers = {'HTTP_AUTHORIZATION': 'JWT ' + res.data["access"],}
        res2 = self.client.get(self.check_staff, auth_headers)
        self.assertEqual(res2.status_code, 401)
    def test_IsStaff_for_staff_user(self):
        response2 = self.client.post(self.register, self.user_data2, format ="json")
        email2 = response2.data['email']
        user2 = get_object_or_404(User, email=email2)
        user2.is_active = True
        user2.is_staff = True
        user2.is_admin = False
        user2.save()
        res = self.client.post(self.login, self.user_data2, format ="json")
        auth_headers = {'HTTP_AUTHORIZATION': 'JWT ' + res.data["access"],}
        res2 = self.client.get(self.check_staff, **auth_headers)
        self.assertEqual(res2.status_code, 200)
    def test_IsStaff_for_admin_user(self):
        response3 = self.client.post(self.register, self.user_data3, format ="json")
        email3 = response3.data['email']
        user3 = get_object_or_404(User, email=email3)
        user3.is_active = True
        user3.is_staff = True
        user3.is_admin = True
        user3.save()
        res = self.client.post(self.login, self.user_data3, format ="json")
        auth_headers = {'HTTP_AUTHORIZATION': 'JWT ' + res.data["access"],}
        res2 = self.client.get(self.check_staff, **auth_headers)
        self.assertEqual(res2.status_code, 200)

    def test_all_endpoints_for_unauthenticated_user(self):
        res = self.client.get(self.check_staff)
        self.assertEqual(res.status_code, 401)
        res = self.client.get(self.delete_user)
        self.assertEqual(res.status_code, 401)