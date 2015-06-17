# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_flatpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='article',
            field=models.ManyToManyField(to='myapp.Article'),
        ),
    ]
