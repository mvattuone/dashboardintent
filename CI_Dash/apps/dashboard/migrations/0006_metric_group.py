# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20151204_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='group',
            field=models.ForeignKey(default=1, to='dashboard.Group'),
            preserve_default=False,
        ),
    ]
