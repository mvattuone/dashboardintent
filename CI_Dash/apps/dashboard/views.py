import json

from django.conf import settings
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

from models import Metric, MetricKey, Group, Dashboard


# Log in a user and allow them to access dashboard, which contains JS
# that allows for interactivity with different datasets.


def index(request):
    return HttpResponseRedirect('/accounts/login/')


# If the user successfully authenticates
@user_passes_test(lambda u: u.is_superuser or u.is_authenticated())
def dashboard(request, slug):
    if request.user.is_superuser:
        dashboard = Dashboard.objects.get(slug=slug)
    else:
        dashboard = Dashboard.objects.get(user=request.user.id)

    context = {
        'recommendations': dashboard.recommendations,
        'trends': json.dumps([
            {
                "label": "Positive",
                "value": dashboard.trendPositive
            },
            {
                "label": "Negative",
                "value": dashboard.trendNegative
            }
        ]),
        'metric_keys': MetricKey.objects.all()
    }


    return render_to_response('dashboard.html', context,
                              context_instance=RequestContext(request))


# returns HTTPResponse with queryset storing all groups containing requested
# metric
def get_groups(request):
    dashboard = Dashboard.objects.get(user=request.user.id)
    metric = request.POST['metricName']

    groups = dashboard.group_set.filter(metric__key__name=metric).values_list(
                                        'name',
                                        'metric__lowest',
                                        'metric__lower',
                                        'metric__neutral',
                                        'metric__higher',
                                        'metric__highest')
    data = json.dumps(list(groups))
    return HttpResponse(data, content_type="application/json")
