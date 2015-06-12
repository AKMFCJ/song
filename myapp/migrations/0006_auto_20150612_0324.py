# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20150612_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2015, 6, 12, 3, 24, 27, 155028, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 6, 12, 3, 24, 40, 785958, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
