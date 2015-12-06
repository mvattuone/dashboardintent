from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import json


# Dashboard represents the parent model that will be feeded into the view
class Dashboard(models.Model):
    user = models.OneToOneField(User)
    client_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    trendPositive = models.IntegerField(null=True, blank=True)
    trendNegative = models.IntegerField(null=True, blank=True)
    recommendations = models.TextField(null=True, blank=True, help_text="This\
                                       will display in the recommendations\
                                       section for a client's dashboard.")

    def clean(self, *args, **kwargs):
            if self.trendPositive + self.trendNegative > 100:
                raise ValidationError("Negative and positive trend values\
                                       should total less than 100 (i.e. total\
                                       100%)")

            super(Dashboard, self).save(*args, **kwargs)


# A group is defined as a page or web interaction that is being tested.
class Group(models.Model):
    name = models.CharField(max_length=300)
    position = models.PositiveSmallIntegerField()
    dashboard = models.ForeignKey(Dashboard)

    def __unicode__(self):
        return '%s' % self.name

# Metrics are bound to groups and can be added as needed.
# Examples may include brand sentiment and purchase intent
# Currently supports simple 5-column integer line charts


class MetricKey(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s' % self.name


class Metric(models.Model):
    key = models.ForeignKey(MetricKey)
    lowest = models.IntegerField(null=True, blank=True)
    lower = models.IntegerField(null=True, blank=True)
    neutral = models.IntegerField(null=True, blank=True)
    higher = models.IntegerField(null=True, blank=True)
    highest = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(Group)


    def __unicode__(self):
        return '%s' % self.key
