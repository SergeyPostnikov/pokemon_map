# Generated by Django 3.1.14 on 2022-12-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0007_auto_20221227_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
