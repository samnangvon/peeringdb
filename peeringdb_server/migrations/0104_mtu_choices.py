# Generated by Django 3.2.16 on 2022-12-09 12:30

from django.db import migrations, models

def closest_number(numbers, value):
    closest_number = None
    for number in numbers:
        if closest_number is None or abs(value - number) < abs(value - closest_number):
            closest_number = number
    return closest_number

def normalize(apps, schema_editor):

    IXLan = apps.get_model("peeringdb_server", "IXLan")

    values = [1500, 9000]

    for ixlan in IXLan.handleref.filter():
        mtu = ixlan.mtu

        ixlan.mtu = closest_number(values, mtu)
        if mtu != ixlan.mtu:
            ixlan.save()


class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb_server', '0103_mtu_default'),
    ]

    operations = [
        migrations.RunPython(normalize, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='ixlan',
            name='mtu',
            field=models.PositiveIntegerField(choices=[(1500, "1500"), (9000, "9000")], default=1500, verbose_name='MTU'),
        ),
    ]