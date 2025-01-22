from django.test import TestCase
from django.contrib.auth import get_user_model


class ChefModelTest(TestCase):
    fixtures = ["chefs.json"]

    def test_chef_creation(self):
        chef = get_user_model().objects.get(username="fin.zevs")
        self.assertEqual(chef.years_of_experience, 2)
        self.assertEqual(str(chef), "fin.zevs: (Finsar Zevski)")

    def test_get_absolute_url(self):
        chef = get_user_model().objects.get(username="fin.zevs")
        self.assertEqual(chef.get_absolute_url(), f"/chefs/{chef.pk}/")

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
