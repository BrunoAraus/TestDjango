# Generated by Django 3.2.13 on 2022-07-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_plato_patente'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='precio_final',
            field=models.IntegerField(null=True),
        ),
    ]
