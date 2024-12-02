from django.urls import path

from kitchen.views import (
    DishListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishTypeListView,
    DishTypeDetailView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    ChefListView,
    ChefDetailView,
    ChefCreateView,
    ChefDeleteView,
    ChefUpdateView,
    index,
)


urlpatterns = [
    path("", index, name="index"),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish-create",
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update",
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete",
    ),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish_type-list"
    ),
    path(
        "dish_types/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish_type-detail"
    ),
    path(
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish_type-create"
    ),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type-update"
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish_type-delete"
    ),
    path(
        "chefs/",
        ChefListView.as_view(),
        name="chef-list"
    ),
    path(
        "chefs/<int:pk>/",
        ChefDetailView.as_view(),
        name="chef-detail"
    ),
    path(
        "chefs/create/",
        ChefCreateView.as_view(),
        name="chef-create"
    ),
    path(
        "chefs/<int:pk>/delete/",
        ChefDeleteView.as_view(),
        name="chef-delete"
    ),
    path(
        "chefs/<int:pk>/update/",
        ChefUpdateView.as_view(),
        name="chef-update"
    ),
    # path("assign-me-car/<int:pk>/", assign_me_car, name="assign-me-car"),
    # path("delete-me-car/<int:pk>/", delete_me_car, name="delete-me-car")
]

app_name = "kitchen"
