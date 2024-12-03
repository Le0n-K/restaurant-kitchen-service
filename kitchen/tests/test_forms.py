from django.test import TestCase

from kitchen.forms import ChefCreationForm


class FormsTests(TestCase):
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
