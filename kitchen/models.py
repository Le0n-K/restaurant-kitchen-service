from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Chef(AbstractUser):
    years_of_experience = models.IntegerField()


class DishType(models.Model):
    name = models.CharField(max_length=100)


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    chefs = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="chefs")
