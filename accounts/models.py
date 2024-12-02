from django.contrib.auth.models import AbstractUser
from django.db import models


class Chef(AbstractUser):
    years_of_experience = models.IntegerField(default=1)
