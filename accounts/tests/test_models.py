from django.test import TestCase
from accounts.models import Chef


class ChefModelTest(TestCase):
    def setUp(self):
        Chef.objects.create(username="test_chef", years_of_experience=5)

    def test_chef_creation(self):
        chef = Chef.objects.get(username="test_chef")
        self.assertEqual(chef.years_of_experience, 5)
        self.assertEqual(str(chef), "test_chef: ( )")

    def test_get_absolute_url(self):
        chef = Chef.objects.get(username="test_chef")
        self.assertEqual(chef.get_absolute_url(), f"/chefs/{chef.pk}/")
