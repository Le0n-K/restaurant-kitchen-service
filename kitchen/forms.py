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
        fields = "__all__"


class ChefCreationForm(UserCreationForm):
    class Meta:
        model = Chef
        fields = (UserCreationForm.Meta.fields
                  + ("first_name", "last_name", "years_of_experience",))

        def clean_years_of_experience(self):
            years_of_experience = self.cleaned_data["years_of_experience"]
            if years_of_experience < 0:
                raise ValidationError(
                    "Ensure your years of experience are not equal to or greater than zero!"
                )


class ChefExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ("years_of_experience",)

    def clean_years_of_experience(self):
        years_of_experience = self.cleaned_data["years_of_experience"]
        if years_of_experience < 0:
            raise ValidationError(
                "Ensure your years of experience are not equal to or greater than zero!"
            )
