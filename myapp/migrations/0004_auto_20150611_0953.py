# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('myapp', '0003_flatpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='flatpage',
            options={'ordering': ('url',), 'verbose_name': 'flat page', 'verbose_name_plural': 'flat pages'},
        ),
        migrations.AddField(
            model_name='flatpage',
            name='enable_comments',
            field=models.BooleanField(default=False, verbose_name='enable comments'),
        ),
        migrations.AddField(
            model_name='flatpage',
            name='registration_required',
            field=models.BooleanField(default=False, help_text='If this is checked, only logged-in users will be able to view the page.', verbose_name='registration required'),
        ),
        migrations.AddField(
            model_name='flatpage',
            name='sites',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='flatpage',
            name='template_name',
            field=models.CharField(help_text="Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'.", max_length=70, verbose_name='template name', blank=True),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='content',
            field=models.TextField(verbose_name='content', blank=True),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='title',
            field=models.CharField(max_length=200, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='url',
            field=models.CharField(max_length=100, verbose_name='URL', db_index=True),
        ),
        migrations.AlterModelTable(
            name='flatpage',
            table='django_flatpage',
        ),
    ]
