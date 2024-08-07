# Generated by Django 5.0.7 on 2024-07-31 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0008_orders_broker_company_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="broker_company",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="orders",
            name="broker_company_id",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="orders",
            name="broker_sales",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="orders",
            name="dev_sales",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="orders",
            name="dev_sales_manager",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
