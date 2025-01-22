from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class DishTypeListViewTests(TestCase):
    fixtures = ["dish_types.json", "chefs.json"]

    def setUp(self):
        self.user = get_user_model().objects.get(username="fin.zevs")
        self.client.force_login(self.user)

    def test_search_dish_type_by_name(self):
        response = self.client.get(reverse("kitchen:dish-type-list"), {"name": "Dessert"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dessert")
        self.assertNotContains(response, "Alcohol")

    def test_empty_search_returns_all(self):
        response = self.client.get(reverse("kitchen:dish-type-list"), {"name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dessert")
        self.assertContains(response, "Alcohol")


class DishListViewTests(TestCase):
    fixtures = ["dishes.json", "dish_types.json", "chefs.json"]

    def setUp(self):
        self.user = get_user_model().objects.get(username="fin.zevs")
        self.client.force_login(self.user)

    def test_search_dish_by_name(self):
        response = self.client.get(reverse("kitchen:dish-list"), {"name": "BBQ wings"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BBQ wings")
        self.assertNotContains(response, "Pork steak")

    def test_empty_search_returns_all(self):
        response = self.client.get(reverse("kitchen:dish-list"), {"name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BBQ wings")
        self.assertContains(response, "Pork steak")
        self.assertContains(response, "Grilled vegetables")
        self.assertContains(response, "Duck with berries sauce")


class ChefListViewTests(TestCase):
    fixtures = ["chefs.json"]

    def setUp(self):
        self.user = get_user_model().objects.get(username="fin.zevs")
        self.client.force_login(self.user)

    def test_search_chef_by_username(self):
        response = self.client.get(reverse("kitchen:chef-list"), {"username": "fin.zevs"})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fin.zevs")
        self.assertNotContains(response, "hari.klin")

    def test_empty_search_returns_all(self):
        response = self.client.get(reverse("kitchen:chef-list"), {"username": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "fin.zevs")
        self.assertContains(response, "hari.klin")
