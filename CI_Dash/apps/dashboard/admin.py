from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from models import Group, Metric, MetricKey, Dashboard


class MetricInline(NestedStackedInline):
    model = Metric
    fk_name = 'group'


class GroupInline(NestedStackedInline):
    model = Group
    extra = 1
    fk_name = 'dashboard'
    inlines = [MetricInline]


class GroupAdmin(NestedModelAdmin):
    model = Group
    inlines = [MetricInline]


class DashboardAdmin(NestedModelAdmin):
    model = Dashboard
    inlines = [GroupInline]
    prepopulated_fields = {"slug": ("client_name",)}

admin.site.register(MetricKey)
admin.site.register(Dashboard, DashboardAdmin)
