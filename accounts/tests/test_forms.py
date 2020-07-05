from django.test import TestCase
from django import forms 
from django.contrib.auth.models import User

from accounts.forms import UserLoginForm, UserRegistrationForm

class TestUserLoginForm(TestCase):
    
    def setUp(self):
        self.form = UserLoginForm()

    def test_username_or_email_label(self):
        self.assertEqual(self.form.fields["username_or_email"].label, "username or email")

    def test_password_label(self):
        self.assertEqual(self.form.fields["password"].label, "password")


class TestUserRegistrationForm(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user("booboo", email="where@ever.com")

    def setUp(self):
        self.form = UserRegistrationForm()

    def test_username_label(self):
        self.assertEqual(self.form.fields["username"].label, "Username")

    def test_email_label(self):
        self.assertEqual(self.form.fields["email"].label, "Email address")

    def test_password1_label(self):
        self.assertEqual(self.form.fields["password1"].label, "Password")

    def test_password2_label(self):
        self.assertEqual(self.form.fields["password2"].label, "Password Confirmation")

    # def test_clean_email(self):
    #     form = UserRegistrationForm({
    #         "username": "newy",
    #         "email": "where@ever.com",
    #     })
    #     self.assertRaises(forms.ValidationError, form.clean_email)
