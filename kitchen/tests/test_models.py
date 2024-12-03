from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Dish, DishType
from accounts.models import Chef


class ModelTests(TestCase):
    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test Dish Type"
        )
        dish = Dish.objects.create(
            name="test",
            dish_type=dish_type,
            price=13.55
        )
        self.assertEqual(
            str(dish), f"{dish.name}: {dish.price}"
        )

    def test_chef_str(self):
        chef = get_user_model().objects.create(
            username="bob.res",
            first_name="Bob",
            last_name="Reswill"
        )
        self.assertEqual(
            str(chef),
            f"{chef.username} ({chef.first_name} {chef.last_name})"
        )

    def test_create_chef_with_years_of_experience(self):
        username = "gig.mad"
        years_of_experience = 4
        password = "gh61ha34"
        chef = get_user_model().objects.create_user(
            username=username,
            years_of_experience=years_of_experience,
            password=password
        )
        self.assertEqual(chef.username, username)
        self.assertEqual(chef.years_of_experience, years_of_experience)
        self.assertTrue(chef.check_password(password))

    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Bakery"
        )
        self.assertEqual(
            str(dish_type),
            f"{dish_type.name}"
        )
