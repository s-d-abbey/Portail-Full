# Generated by Django 4.1.4 on 2023-02-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magasin_day_value',
            name='week',
            field=models.IntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='magasin_value',
            name='week',
            field=models.IntegerField(default=8),
        ),
        migrations.AlterField(
            model_name='magasin_weekly',
            name='week',
            field=models.IntegerField(default=8),
        ),
    ]