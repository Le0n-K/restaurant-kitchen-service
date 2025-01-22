from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    fixtures = ["dish_types.json", "chefs.json"]

    def setUp(self):
        self.user = get_user_model().objects.get(username="fin.zevs")
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        response = self.client.get(reverse("kitchen:dish-type-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["dish_type_list"]), 3)
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")


class PrivateChefTests(TestCase):
    fixtures = ["chefs.json"]

    def setUp(self):
        self.user = get_user_model().objects.get(username="fin.zevs")
        self.client.force_login(self.user)

    def test_create_chef(self):
        form_data = {
            "username": "tom.li",
            "password1": "zxzx1212",
            "password2": "zxzx1212",
            "first_name": "Tom",
            "last_name": "Li",
            "years_of_experience": 8
        }
        self.client.post(reverse("kitchen:chef-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.years_of_experience, form_data["years_of_experience"])
