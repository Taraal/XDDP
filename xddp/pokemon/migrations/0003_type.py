# Generated by Django 3.0.3 on 2020-02-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20200119_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.IntegerField(null=True)),
                ('nom', models.CharField(max_length=50, null=True)),
                ('double_damage_from', models.ManyToManyField(related_name='_type_double_damage_from_+', to='pokemon.Type')),
            ],
        ),
    ]
