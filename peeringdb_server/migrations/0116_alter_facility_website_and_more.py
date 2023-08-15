# Generated by Django 4.2.3 on 2023-07-13 12:09

import django_peeringdb.models.abstract
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0115_hash_oauth_client_secret"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="website",
            field=models.URLField(blank=True, default="", verbose_name="Website"),
        ),
        migrations.AlterField(
            model_name="internetexchange",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, default="", verbose_name="Company Website"
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="website",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, default="", verbose_name="Website"
            ),
        ),
    ]
