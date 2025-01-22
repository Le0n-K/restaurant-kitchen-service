from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Chef(AbstractUser):
    years_of_experience = models.IntegerField(default=1, null=True, blank=True)

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("kitchen:chef-detail", kwargs={"pk": self.pk})

    def clean_years_of_experience(self):
        if self.years_of_experience is None:
            raise ValidationError("Years of experience is required.")
        if self.years_of_experience <= 0:
            raise ValidationError("Ensure your years of experience are greater than zero!")
        return self.years_of_experience
