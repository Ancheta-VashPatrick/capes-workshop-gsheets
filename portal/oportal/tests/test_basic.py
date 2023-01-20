from django.test import TestCase

"""
Credits to Mozilla Development Network for the entire code and some comments
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
"""
class BasicTest(TestCase):
    # Use this setup method if the data will not be modified in any of the tests
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    # Use this setup method to create a new set of data every test
    def setUp(self):
        # print("setUp: Run once for every test method to setup clean data.")
        pass
    
    # False is not equal to True hence this test will fail
    def test_that_will_fail(self):
        # print("Method: test_that_will_fail")
        self.assertTrue(False)

    # True is equal to True hence this test will succeed
    def test_that_will_succeed(self):
        # print("Method: test_that_will_succeed")
        self.assertTrue(True)

    # This test will succeed since 1 + 1 = 2
    def test_basic_math(self):
        # print("Method: test_basic_math")
        self.assertEqual(1 + 1, 2)