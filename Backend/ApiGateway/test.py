try:
    from api import app
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
        response = tester.get("/user/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

if __name__ == "__main__":
    unittest.main()