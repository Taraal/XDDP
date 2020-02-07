# Generated by Django 3.0.2 on 2020-02-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0002_auto_20200119_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('min_level', models.IntegerField(null=True)),
                ('max_level', models.IntegerField(null=True)),
                ('allowed_pokemon', models.ManyToManyField(to='pokemon.Pokemon')),
            ],
        ),
    ]
