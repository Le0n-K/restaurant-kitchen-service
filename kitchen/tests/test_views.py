from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from kitchen.models import DishType

DISH_TYPE_URL = reverse("kitchen:dish-type-list")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DISH_TYPE_URL)
        self.assertNotEqual(res.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user.tu",
            password="u1s2e3r4"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Fruits")
        DishType.objects.create(name="Snacks")

        response = self.client.get(DISH_TYPE_URL)
        self.assertEqual(response.status_code, 200)
        dish_types = DishType.objects.all()
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types),
        )
        self.assertTemplateUsed(
            response,
            "kitchen/dish_type_list.html"
        )


class PrivateChefTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="user.tu",
            password="u1s2e3r4"
        )
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
