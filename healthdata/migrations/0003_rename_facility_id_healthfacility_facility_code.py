# Generated by Django 5.1.5 on 2025-02-13 04:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("healthdata", "0002_remove_healthfacility_rating_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="healthfacility",
            old_name="facility_id",
            new_name="facility_code",
        ),
    ]
