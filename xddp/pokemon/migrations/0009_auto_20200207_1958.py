# Generated by Django 3.0.2 on 2020-02-07 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0008_pokemon_current_hp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='nom',
            new_name='name',
        ),
    ]
