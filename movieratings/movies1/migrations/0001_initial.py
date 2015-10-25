# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('movie', models.CharField(max_length=200)),
                ('release_data', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=5)),
                ('occupation', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('rating', models.IntegerField()),
                ('movie', models.ForeignKey(to='movies1.Movie')),
                ('rater', models.ForeignKey(to='movies1.Rater')),
            ],
        ),
    ]
