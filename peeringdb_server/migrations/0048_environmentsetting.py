# Generated by Django 2.2.14 on 2020-07-24 12:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0047_ixf_import_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="EnvironmentSetting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "setting",
                    models.CharField(
                        choices=[
                            (
                                "IXF_IMPORTER_DAYS_UNTIL_TICKET",
                                "IX-F Importer: Days until DeskPRO ticket is created",
                            )
                        ],
                        max_length=255,
                        unique=True,
                    ),
                ),
                ("value_str", models.CharField(blank=True, max_length=255, null=True)),
                ("value_int", models.IntegerField(blank=True, null=True)),
                ("value_bool", models.BooleanField(blank=True, default=False)),
                ("value_float", models.FloatField(blank=True, null=True)),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, null=True, verbose_name="Last Updated"
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="Configured on"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        help_text="Last updated by this user",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="admincom_setting_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Environment Setting",
                "verbose_name_plural": "Environment Settings",
                "db_table": "peeringdb_settings",
            },
        ),
    ]
