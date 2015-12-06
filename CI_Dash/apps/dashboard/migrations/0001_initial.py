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
            name='Dashboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('client_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
                ('trendPositive', models.IntegerField(null=True, blank=True)),
                ('trendNegative', models.IntegerField(null=True, blank=True)),
                ('recommendations', models.TextField(help_text=b"This                                       will display in the recommendations                                       section for a client's dashboard.", null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('position', models.PositiveSmallIntegerField()),
                ('dashboard', models.ForeignKey(to='dashboard.Dashboard')),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lowest', models.IntegerField(null=True, blank=True)),
                ('lower', models.IntegerField(null=True, blank=True)),
                ('neutral', models.IntegerField(null=True, blank=True)),
                ('higher', models.IntegerField(null=True, blank=True)),
                ('highest', models.IntegerField(null=True, blank=True)),
                ('group', models.ForeignKey(to='dashboard.Group')),
            ],
        ),
        migrations.CreateModel(
            name='MetricKey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='metric',
            name='key',
            field=models.ForeignKey(to='dashboard.MetricKey'),
        ),
    ]
