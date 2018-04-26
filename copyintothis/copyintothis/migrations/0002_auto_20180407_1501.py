# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='message',
            field=models.CharField(default='blue whale', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='subject',
            field=models.CharField(default='blue whale', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='to',
            field=models.CharField(default='blue whale', max_length=120),
            preserve_default=False,
        ),
    ]
