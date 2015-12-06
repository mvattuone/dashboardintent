# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_auto_20151204_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metric',
            old_name='name',
            new_name='metric',
        ),
    ]
