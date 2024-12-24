# Generated by Django 5.1.3 on 2024-12-02 12:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_dish_options_alter_dishtype_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dish",
            name="chefs",
        ),
        migrations.AddField(
            model_name="dish",
            name="chefs",
            field=models.ManyToManyField(
                related_name="chefs", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
