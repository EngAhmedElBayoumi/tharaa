# Generated by Django 5.0.7 on 2024-07-31 17:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0006_thraa_info"),
    ]

    operations = [
        migrations.AddField(
            model_name="thraa_info",
            name="broker_company_id",
            field=models.CharField(default=1, max_length=10000),
            preserve_default=False,
        ),
    ]
