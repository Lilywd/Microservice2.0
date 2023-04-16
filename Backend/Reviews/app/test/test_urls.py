from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app import views


class TestUrls(SimpleTestCase):

    def test_product_comments_create_url(self):
        url = reverse("product_comments_create")
        self.assertEquals(resolve(url).func.view_class, views.ProductCommentsCreate)

    def test_product_comments_deletes_url(self):
        url = reverse("product_comments_deletes", kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ProductCommentsDelete)

    def test_user_comments_deletes_url(self):
        url = reverse("user_comments_deletes", kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UserCommentsDelete)

    def test_single_product_url(self):
        url = reverse("single_product", kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.ProductComments)

    def test_delete_comment_details_url(self):
        url = reverse("delete_comment", kwargs={'pk': 1, 'ui' : 1})
        self.assertEquals(resolve(url).func.view_class, views.UserProductComments)
