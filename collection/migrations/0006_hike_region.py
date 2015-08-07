# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20150725_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='hike',
            name='region',
            field=models.CharField(default='Portland', max_length=255),
            preserve_default=False,
        ),
    ]
