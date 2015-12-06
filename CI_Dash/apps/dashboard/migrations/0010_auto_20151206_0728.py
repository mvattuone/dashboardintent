# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20151206_0452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metric',
            old_name='average',
            new_name='neutral',
        ),
    ]
