# Generated by Django 3.1.14 on 2023-01-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20230106_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='kind',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entities', to='pokemon_entities.pokemon', verbose_name='Вид'),
        ),
    ]
