# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2020-09-21 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NamesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=120, null=True)),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('year', models.CharField(blank=True, max_length=120, null=True)),
            ],
        ),
    ]