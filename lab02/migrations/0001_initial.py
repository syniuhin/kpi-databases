# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-21 08:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('year_created', models.DateField()),
                ('version', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('lat', models.FloatField(max_length=10)),
                ('lng', models.FloatField(max_length=10)),
                ('accessible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('aperture', models.FloatField()),
                ('iso', models.IntegerField()),
                ('shot_time', models.DateTimeField()),
                ('camera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab02.Camera')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab02.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('level', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('cameras', models.ManyToManyField(to='lab02.Camera')),
                ('locations', models.ManyToManyField(to='lab02.Location')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='photographer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lab02.Photographer'),
        ),
    ]
