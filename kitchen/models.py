from django.conf import settings
from django.db import models


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return str(self.name)


class Dish(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dishes")
    chefs = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dishes")

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return f"{self.name}: {self.price}"
