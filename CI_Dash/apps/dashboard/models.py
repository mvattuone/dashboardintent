from django.db import models
from django.contrib.auth.models import User

import json

# A group is defined as a page or web interaction that is being tested.
# Clients are simply users associated with the group.


class Group(models.Model):
    name = models.CharField(max_length=300)
    position = models.PositiveSmallIntegerField()
    client = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

# Metrics are bound to groups and can be added as needed.
# Examples may include brand sentiment and purchase intent
# Currently supports simple 5-column integer line charts


class Metric(models.Model):
    name = models.CharField(max_length=300)
    lowest = models.IntegerField(null=True, blank=True)
    lower = models.IntegerField(null=True, blank=True)
    average = models.IntegerField(null=True, blank=True)
    higher = models.IntegerField(null=True, blank=True)
    highest = models.IntegerField(null=True, blank=True)
    group = models.ForeignKey(Group)

    def __unicode__(self):
        return self.name
