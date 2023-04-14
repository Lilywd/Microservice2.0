from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app import views


class TestUrls(SimpleTestCase):

    def test_ping_url(self):
        url = reverse("ping")
        self.assertEquals(resolve(url).func, views.ping)
    def test_isAdmin_url(self):
        url = reverse("is-admin")
        self.assertEquals(resolve(url).func, views.IsAdmin)
    def test_IsStaff_url(self):
        url = reverse("is-staff")
        self.assertEquals(resolve(url).func, views.IsStaff)

    def test_deleteUser_url(self):
        url = reverse("delete-user")
        self.assertEquals(resolve(url).func, views.deleteUser)

    def test_addAdmin_url(self):
        url = reverse("add-admin")
        self.assertEquals(resolve(url).func, views.addAdmin)

    def test_removeAdmin_url(self):
        url = reverse("remove-admin")
        self.assertEquals(resolve(url).func, views.removeAdmin)

    def test_addStaff_url(self):
        url = reverse("add-staff")
        self.assertEquals(resolve(url).func, views.addStaff)

    def test_removeStaff_url(self):
        url = reverse("remove-staff")
        self.assertEquals(resolve(url).func, views.removeStaff)
    def test_UpdateProfile_url(self):
        url = reverse("update_profile")
        self.assertEquals(resolve(url).func.view_class, views.UpdateProfile)
