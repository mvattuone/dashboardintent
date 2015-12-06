# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20151203_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='client',
            field=models.ForeignKey(default=1, to='dashboard.Client'),
            preserve_default=False,
        ),
    ]
