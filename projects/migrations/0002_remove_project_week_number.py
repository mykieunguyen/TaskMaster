# Generated by Django 4.2.2 on 2023-06-07 15:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="week_number",
        ),
    ]
