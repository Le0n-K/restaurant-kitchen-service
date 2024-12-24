from django.contrib import admin

from .models import Dish, DishType


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("dish_type",)


admin.site.register(DishType)
