from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from accounts.models import Chef
from kitchen.models import Dish


class DishForm(forms.ModelForm):
    chefs = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = ("name", "description", "price", "dish_type", "chefs",)


class ChefCreationForm(UserCreationForm):
    class Meta:
        model = Chef
        fields = (UserCreationForm.Meta.fields
                  + ("first_name", "last_name", "years_of_experience",))

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("years_of_experience", )
        if years_of_experience is None:
            raise ValidationError("This field is required.")
        if years_of_experience <= 0:
            raise ValidationError(
                "Ensure your years of experience are greater than zero!"
            )
        return years_of_experience


class ChefExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ("first_name", "last_name", "email", "years_of_experience",)

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data.get("years_of_experience",)
        if years_of_experience is None:
            raise ValidationError("This field is required.")
        if years_of_experience <= 0:
            raise ValidationError(
                "Ensure your years of experience are greater than zero!"
            )
        return years_of_experience


class ChefSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"})
    )


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"})
    )
