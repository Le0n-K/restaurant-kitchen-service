from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminSiteTest(TestCase):
    fixtures = ["chefs.json"]

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="adminpass123"
        )
        self.client.force_login(self.admin_user)
        self.chef = get_user_model().objects.get(username="fin.zevs")

    def test_chef_years_of_experience(self):
        url = reverse("admin:accounts_chef_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.chef.years_of_experience)

    def test_chef_detail_years_of_experience(self):
        url = reverse("admin:accounts_chef_change", args=[self.chef.id])
        res = self.client.get(url)
        self.assertContains(res, self.chef.years_of_experience)
