# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('position', models.PositiveSmallIntegerField()),
                ('client', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('lowest', models.IntegerField(null=True, blank=True)),
                ('lower', models.IntegerField(null=True, blank=True)),
                ('average', models.IntegerField(null=True, blank=True)),
                ('higher', models.IntegerField(null=True, blank=True)),
                ('highest', models.IntegerField(null=True, blank=True)),
                ('group', models.ForeignKey(to='dashboard.Group')),
            ],
        ),
    ]
