# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trendPositive', models.IntegerField(null=True, blank=True)),
                ('trendNegative', models.IntegerField(null=True, blank=True)),
                ('recommendations', models.TextField(help_text=b"This                                       will display in the recommendations                                       section for a client's dashboard.", null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='client',
            field=models.ForeignKey(to='dashboard.Client'),
        ),
    ]
