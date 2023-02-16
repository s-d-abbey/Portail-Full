# Generated by Django 4.1.4 on 2023-02-16 21:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Magasin_weekly',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('week', models.IntegerField(default=7)),
                ('magasin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.magasin')),
            ],
        ),
        migrations.CreateModel(
            name='Magasin_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=50)),
                ('prenom', models.CharField(blank=True, max_length=50)),
                ('clients_no', models.IntegerField(null=True)),
                ('value', models.IntegerField()),
                ('day', models.DateField(default=datetime.date.today)),
                ('week', models.IntegerField(default=7)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('magasin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.magasin')),
            ],
            options={
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='Magasin_day_value',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(default=7)),
                ('mon', models.IntegerField(blank=True, default=None, null=True)),
                ('tue', models.IntegerField(blank=True, default=None, null=True)),
                ('wed', models.IntegerField(blank=True, default=None, null=True)),
                ('thur', models.IntegerField(blank=True, default=None, null=True)),
                ('fri', models.IntegerField(blank=True, default=None, null=True)),
                ('sat', models.IntegerField(blank=True, default=None, null=True)),
                ('sun', models.IntegerField(blank=True, default=None, null=True)),
                ('magasin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.magasin')),
            ],
        ),
    ]
