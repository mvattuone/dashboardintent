# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_metric_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trendPositive', models.IntegerField(null=True, blank=True)),
                ('trendNegative', models.IntegerField(null=True, blank=True)),
                ('recommendations', models.TextField(help_text=b"This                                       will display in the recommendations                                       section for a client's dashboard.", null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MetricType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.RemoveField(
            model_name='group',
            name='client',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='client',
        ),
        migrations.RemoveField(
            model_name='metric',
            name='group',
        ),
        migrations.AlterField(
            model_name='metric',
            name='name',
            field=models.ForeignKey(to='dashboard.MetricType'),
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.AddField(
            model_name='group',
            name='dashboard',
            field=models.OneToOneField(default=1, to='dashboard.Dashboard'),
            preserve_default=False,
        ),
    ]
