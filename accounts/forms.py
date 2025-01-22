from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from django.core.exceptions import ValidationError

from accounts.models import Chef


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


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def save(self, commit=True):
        try:
            with transaction.atomic():
                user = super().save(commit=False)
                user.email = self.cleaned_data["email"]
                if commit:
                    user.save()
                return user
        except Exception as e:
            raise forms.ValidationError(
                f"An error occurred while saving the user: {str(e)}"
            )
