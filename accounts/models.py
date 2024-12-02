from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Chef(AbstractUser):
    years_of_experience = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen:chef-detail", kwargs={"pk": self.pk})
