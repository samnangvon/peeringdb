# Generated by Django 3.2.9 on 2022-02-02 13:59

import django.core.validators
import django_inet.models
import django_peeringdb.models.abstract
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0080_environmentalsetting_api_throttle"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="status_dashboard",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, null=True, verbose_name="Status Dashboard"
            ),
        ),
        migrations.AddField(
            model_name="internetexchange",
            name="status_dashboard",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, null=True, verbose_name="Status Dashboard"
            ),
        ),
        migrations.AddField(
            model_name="network",
            name="status_dashboard",
            field=django_peeringdb.models.abstract.URLField(
                blank=True, max_length=255, null=True, verbose_name="Status Dashboard"
            ),
        ),
    ]
