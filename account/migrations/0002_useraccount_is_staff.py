# Generated by Django 4.2.3 on 2023-07-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="useraccount",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
    ]
