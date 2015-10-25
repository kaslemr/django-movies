# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies1', '0003_auto_20151023_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='zip_code',
            field=models.CharField(max_length=10),
        ),
    ]
