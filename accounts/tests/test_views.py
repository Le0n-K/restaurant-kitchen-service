from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import Chef


class AccountViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("accounts:register")
        self.login_url = reverse("accounts:login")
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password1": "testpassword123",
            "password2": "testpassword123",
            "years_of_experience": 5
        }

    def test_register_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")

    def test_register_view_POST_valid(self):
        response = self.client.post(self.register_url, self.user_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Chef.objects.filter(username="testuser").exists())

    def test_login_view(self):
        Chef.objects.create_user(username="testuser", email="testuser@example.com", password="testpassword123")
        response = self.client.post(self.login_url, {"username": "testuser", "password": "testpassword123"})
        self.assertEqual(response.status_code, 302)
