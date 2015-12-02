from django.contrib import admin
from models import Group, Metric


class MetricInline(admin.TabularInline):
    model = Metric
    fields = ('name',
              'lowest',
              'lower',
              'average',
              'higher',
              'highest')


class GroupAdmin(admin.ModelAdmin):

    inlines = [MetricInline]

admin.site.register(Group, GroupAdmin)
