# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_metric_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashboard',
            name='client_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='slug',
            field=models.SlugField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='dashboard',
            field=models.ForeignKey(to='dashboard.Dashboard'),
        ),
    ]
