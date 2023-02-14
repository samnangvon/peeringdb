# Generated by Django 3.2.14 on 2022-08-23 16:05

import django.db.models.deletion
from django.db import migrations, models
from django.utils import timezone


def create_email_address_data(apps, schema_editor):
    EmailAddress = apps.get_model("account", "EmailAddress")
    EmailAddressData = apps.get_model("peeringdb_server", "EmailAddressData")

    now = timezone.now()

    for email_address in EmailAddress.objects.filter(verified=True):
        EmailAddressData.objects.create(email=email_address, confirmed_date=now)


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_email_max_length"),
        ("peeringdb_server", "0094_auto_20220823_1331"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailAddressData",
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
                ("confirmed_date", models.DateTimeField(auto_now_add=True)),
                (
                    "email",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="data",
                        to="account.emailaddress",
                    ),
                ),
            ],
            options={
                "db_table": "peeringdb_email_address_data",
            },
        ),
        migrations.RunPython(create_email_address_data, migrations.RunPython.noop),
    ]
