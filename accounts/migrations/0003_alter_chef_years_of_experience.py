# Generated by Django 5.1.3 on 2024-12-03 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_chef_years_of_experience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="chef",
            name="years_of_experience",
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
