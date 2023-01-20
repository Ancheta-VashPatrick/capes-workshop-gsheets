from django.test import TestCase

from ..forms import RegistrationForm

from django.contrib.auth import get_user_model

User = get_user_model()
class RegistrationFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username="test1", password="123") # Note that this user does not have a hashed password

    # Checks if the 'clean_username' validator detects existing usernames
    # This test will fail because user with username 'test1' is already created
    def test_clean_username(self):
        # Fills the form's fields programatically 
        form = RegistrationForm(data={
            'username' : "test1",
            'password' : "123",
            'confirm_password' : "123",
        })

        self.assertTrue(form.is_valid())

    # Checks if the 'clean_confirm_password' validator detects mismatch in the 'password' and 'confirm_password' fields
    # This test will fail because the said fields do not match in this test
    def test_clean_confirm_password(self):
        # Fills the form's fields programatically 
        form = RegistrationForm(data={
            'username' : "test2",
            'password' : "123",
            'confirm_password' : "1234",
        })

        self.assertTrue(form.is_valid())

    # Checks if the 'save' function is able to create a new user
    # This test will succeed
    def test_save(self):
        # Fills the form's fields programatically 
        form = RegistrationForm(data={
            'username' : "test2",
            'password' : "123",
            'confirm_password' : "123",
        })
        
        if form.is_valid():
            form.save()

        user_count = User.objects.all().count()

        self.assertEqual(user_count, 2) # Checks if there are 2 users after saving the form