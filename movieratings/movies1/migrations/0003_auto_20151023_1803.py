# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

from playdata import load_data_movies

class Migration(migrations.Migration):

    dependencies = [
        ('movies1', '0002_auto_20151023_1802'),
    ]

    operations = [
        migrations.RunPython(load_data_movies)
    ]