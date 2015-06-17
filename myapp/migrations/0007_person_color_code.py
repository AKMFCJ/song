# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20150612_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='color_code',
            field=models.CharField(default=datetime.datetime(2015, 6, 12, 7, 28, 2, 156868, tzinfo=utc), max_length=6),
            preserve_default=False,
        ),
    ]
