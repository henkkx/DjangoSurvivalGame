# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 12:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_awarded', models.DateField(default='2019-03-19')),
            ],
        ),
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=254)),
                ('criteria', models.IntegerField(default=10)),
                ('badge_type', models.CharField(max_length=32)),
                ('icon', models.ImageField(blank=True, upload_to='badge_icons')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('games_played', models.IntegerField(default=0)),
                ('most_days_survived', models.IntegerField(default=0)),
                ('most_kills', models.IntegerField(default=0)),
                ('most_people', models.IntegerField(default=0)),
                ('most_exp', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='achievement',
            name='badge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Game.Badge'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Game.Player'),
        ),
    ]
