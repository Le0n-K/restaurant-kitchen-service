from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import Dish, DishType


class ModelTests(TestCase):
    fixtures = ["dishes.json", "dish_types.json", "chefs.json"]

    def test_dish_str(self):
        dish = Dish.objects.get(name="BBQ wings")
        self.assertEqual(str(dish), "BBQ wings: 10.50")

    def test_chef_str(self):
        chef = get_user_model().objects.get(username="fin.zevs")
        self.assertEqual(str(chef), "fin.zevs: (Finsar Zevski)")

    def test_dish_type_str(self):
        dish_type = DishType.objects.get(name="Dessert")
        self.assertEqual(str(dish_type), "Dessert")
