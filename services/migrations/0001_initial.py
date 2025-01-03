# Generated by Django 5.1.2 on 2024-10-18 19:41

import public.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("display_name", models.CharField(max_length=100)),
                (
                    "image",
                    models.FileField(
                        upload_to="services/thumbnails",
                        validators=[public.validators.validate_icon_file_extension],
                    ),
                ),
                ("description", models.TextField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
