from django.test import TestCase
from accounts.forms import RegisterForm


class RegisterFormTest(TestCase):
    def test_register_form_valid(self):
        form_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "years_of_experience": 5
        }
        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_password_mismatch(self):
        form_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "testpassword123",
            "password2": "testpassword456",
            "years_of_experience": 5
        }
        form = RegisterForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)
