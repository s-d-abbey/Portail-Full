# Generated by Django 4.1.4 on 2023-02-26 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magboard', '0003_alter_magasin_day_value_fri_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='magasin_day_value',
            name='week',
            field=models.IntegerField(default=8),
        ),
    ]