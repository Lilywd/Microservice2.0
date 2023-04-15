try:
    from notification_project import app
    import unittest
except Exception as e:
    print("Some Modules are missing {}".format(e))
class TestSetup(unittest.TestCase):
    def setUp(self):
        return super().setUp()
    def tearDown(self):
        return super().tearDown()
class FlaskTest(TestSetup):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    def test_index_post(self):
        tester = app.test_client(self)
        response = tester.post("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_index_put(self):
        tester = app.test_client(self)
        response = tester.put("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_index_delete(self):
        tester = app.test_client(self)
        response = tester.delete("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_index_patch(self):
        tester = app.test_client(self)
        response = tester.patch("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_index_content_type(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.content_type, "application/json")
    def test_index_content_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'message' in response.data)

class TestContact(TestSetup):
    def test_contact_get(self):
        tester = app.test_client(self)
        response = tester.get("/contact")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_contact_put(self):
        tester = app.test_client(self)
        response = tester.put("/contact")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_contact_patch(self):
        tester = app.test_client(self)
        response = tester.patch("/contact")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_contact_delete(self):
        tester = app.test_client(self)
        response = tester.delete("/contact")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_contact_post_with_no_data(self):
        tester = app.test_client(self)
        response = tester.post("/contact")
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    def test_contact_post_with_only_email(self):
        tester = app.test_client(self)
        response = tester.post("/contact", data={"email":"test1234@gmail.com"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    def test_contact_post_with_only_name(self):
        tester = app.test_client(self)
        response = tester.post("/contact", data={"name":"test1234@gmail.com"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    def test_contact_post_with_only_body(self):
        tester = app.test_client(self)
        response = tester.post("/contact", data={"body":"test1234@gmail.com"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    # def test_contact_post_with_complete_data(self):
    #     tester = app.test_client(self)
    #     response = tester.post("/contact", json={"name": "Samson", "email":"akinolasamson1234@gmail.com", "body":"testing"})
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode, 200)

class TestSub(TestSetup):
    def test_sub_get(self):
        tester = app.test_client(self)
        response = tester.get("/sub")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_sub_put(self):
        tester = app.test_client(self)
        response = tester.put("/sub")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_sub_patch(self):
        tester = app.test_client(self)
        response = tester.patch("/sub")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_sub_delete(self):
        tester = app.test_client(self)
        response = tester.delete("/sub")
        statuscode = response.status_code
        self.assertEqual(statuscode, 405)
    def test_sub_post_no_details(self):
        tester = app.test_client(self)
        response = tester.post("/sub")
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    def test_sub_post_with_invalid_email(self):
        tester = app.test_client(self)
        response = tester.post("/sub", json={"email": "samson1234"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 400)
    # def test_sub_post_with_valid_email(self):
    #     tester = app.test_client(self)
    #     response = tester.post("/sub", json={"email": "samsonAkin1234@gmail.com"})
    #     statuscode = response.status_code
    #     self.assertEqual(statuscode, 200)
if __name__ == "__main__":
    unittest.main()