# Generated by Django 5.1.2 on 2024-10-28 05:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0007_category_category_name_store_store_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="store",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="sales.store"
            ),
            preserve_default=False,
        ),
    ]
