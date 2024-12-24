from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from kitchen.models import Dish, DishType
from accounts.models import Chef


class DishTypeListViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="wierd.lp",
            password="123qweasd123"
        )
        self.client.force_login(self.user)

        self.dish_type1 = DishType.objects.create(
            name="Dessert"
        )
        self.dish_type2 = DishType.objects.create(
            name="Alcohol"
        )

    def test_search_dish_type_by_name(self):
        response = self.client.get(reverse("kitchen:dish-type-list"),
                                   {"name": "Dessert"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dessert")
        self.assertNotContains(response, "Alcohol")

    def test_empty_search_returns_all(self):
        response = self.client.get(reverse("kitchen:dish-type-list"),
                                   {"name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dessert")
        self.assertContains(response, "Alcohol")


class DishListViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="x8x.lil",
            password="po09jl87")
        self.client.force_login(self.user)

        self.dish_type = DishType.objects.create(
            name="Grill"
        )
        self.dish1 = Dish.objects.create(
            name="BBQ wings",
            dish_type=self.dish_type,
            price=10.50
        )
        self.dish2 = Dish.objects.create(
            name="Duck with berries sauce",
            dish_type=self.dish_type,
            price=25.00
        )
        self.dish3 = Dish.objects.create(
            name="Grilled vegetables",
            dish_type=self.dish_type,
            price=9.70
        )
        self.dish4 = Dish.objects.create(
            name="Pork steak",
            dish_type=self.dish_type,
            price=15.00
        )

    def test_search_dish_by_model(self):
        response = self.client.get(reverse("kitchen:dish-list"),
                                   {"name": "BBQ wings"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BBQ wings")
        self.assertNotContains(response, "Pork steak")

    def test_empty_search_returns_all(self):
        response = self.client.get(reverse("kitchen:dish-list"),
                                   {"name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BBQ wings")
        self.assertContains(response, "Pork steak")
        self.assertContains(response, "Grilled vegetables")
        self.assertContains(response, "Duck with berries sauce")


class ChefListViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="nika.yer",
            password="fg56sd23vb78")
        self.client.force_login(self.user)

        self.chef1 = Chef.objects.create(
            username="fin.zevs",
            first_name="Finsar",
            last_name="Zevski",
            years_of_experience=2
        )
        self.chef2 = Chef.objects.create(
            username="hari.klin",
            first_name="Harry",
            last_name="Xander",
            years_of_experience=12
        )

    def test_search_chef_by_username(self):
        response = self.client.get(reverse("kitchen:chef-list"),
                                   {"username": "fin.zevs"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fin.zevs")
        self.assertNotContains(response, "hari.klin")

    def test_empty_search_returns_all(self):
        response = self.client.get(reverse("kitchen:chef-list"),
                                   {"username": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fin.zevs")
        self.assertContains(response, "hari.klin")
