# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20151206_0451'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MetricType',
            new_name='MetricKey',
        ),
        migrations.RenameField(
            model_name='metric',
            old_name='metric',
            new_name='key',
        ),
    ]
