# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_auto_20180407_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='subject',
            field=models.CharField(max_length=120, blank=True),
        ),
    ]
