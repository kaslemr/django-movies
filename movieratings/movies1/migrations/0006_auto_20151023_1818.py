# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from playdata import load_data_ratings


class Migration(migrations.Migration):

    dependencies = [
        ('movies1', '0005_auto_20151023_1816'),
    ]

    operations = [
        migrations.RunPython(load_data_ratings)
    ]
