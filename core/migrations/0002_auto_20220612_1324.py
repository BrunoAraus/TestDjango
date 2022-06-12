# Generated by Django 3.2.13 on 2022-06-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='patente',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='plato',
            name='imagen',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
