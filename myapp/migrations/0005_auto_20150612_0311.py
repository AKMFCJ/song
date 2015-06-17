# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20150611_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='registration_required',
            field=models.BooleanField(default=True, help_text='If this is checked, only logged-in users will be able to view the page.', verbose_name='registration required'),
        ),
    ]
