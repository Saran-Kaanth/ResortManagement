# Generated by Django 4.2 on 2023-04-20 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rooms",
            name="room_no",
            field=models.CharField(
                max_length=10, primary_key=True, serialize=False, verbose_name="Room No"
            ),
        ),
        migrations.AlterField(
            model_name="rooms",
            name="room_type",
            field=models.TextField(
                choices=[
                    ("Premium", "Premium"),
                    ("Classic", "Classic"),
                    ("Cottage", "Cottage"),
                ],
                default="Classic",
                max_length=30,
            ),
        ),
    ]
