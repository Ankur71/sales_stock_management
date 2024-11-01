# Generated by Django 5.1.2 on 2024-10-28 05:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sales", "0005_remove_product_vendor_remove_product_profit_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vendor",
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
                ("vendor_number", models.CharField(max_length=100)),
                ("vendor_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="product",
            name="vendor_name",
        ),
        migrations.AddField(
            model_name="product",
            name="vendor",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="sales.vendor",
            ),
            preserve_default=False,
        ),
    ]
