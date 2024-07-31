# Generated by Django 5.0.7 on 2024-07-31 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_orders_branch"),
    ]

    operations = [
        migrations.CreateModel(
            name="Units_num",
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
                ("uints_num", models.CharField(default="1003", max_length=50)),
                ("sympol", models.CharField(default="EOI", max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name="customers_num",
            name="sympol",
            field=models.CharField(default="G", max_length=10),
        ),
        migrations.AddField(
            model_name="orders",
            name="broker_id",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="customers_num",
            name="customer_num",
            field=models.CharField(default="1002", max_length=50),
        ),
    ]
