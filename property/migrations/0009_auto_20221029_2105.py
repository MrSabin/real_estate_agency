# Generated by Django 2.2.24 on 2022-10-29 18:05

from django.db import migrations


def get_flat_owners(apps, schema_editor):
    flats = apps.get_model("property", "Flat")
    owners = apps.get_model("property", "Owner")
    for owner in owners.objects.all():
        finded_flats = flats.objects.filter(owner=owner.full_name)
        owner.owned_flats.set(finded_flats)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20221029_1549'),
    ]

    operations = [
        migrations.RunPython(get_flat_owners)
    ]
