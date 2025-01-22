from django.test import TestCase

from accounts.forms import RegisterForm, ChefCreationForm


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


class ChefCreationFormTest(TestCase):
    def test_chef_creation_form_is_valid(self):
        form_data = {
            "username": "stiven.rou",
            "password1": "a0s9d8f7",
            "password2": "a0s9d8f7",
            "first_name": "Steven",
            "last_name": "Rouli",
            "years_of_experience": 7
        }
        form = ChefCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
