# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_hike_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='description',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Name', max_length=255),
            preserve_default=False,
        ),
    ]
