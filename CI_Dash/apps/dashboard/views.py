from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import Metric, Group
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

import json

# Log in a user and allow them to access dashboard, which contains JS
# that allows for interactivity with different datasets.


@login_required(login_url='/accounts/login/')
def index(request):

    context = {
        'metrics': Metric.objects.all().values('name').distinct()
    }
    print context
    return render_to_response('dashboard.html', context,
                              context_instance=RequestContext(request))

# Takes a requested metric passed in via POST and retrieves all associated grou
# ps containing the metric, along with JSON serializable metric values for each
# group returned.


@csrf_exempt
def retrieve(request):
    qs = Group.objects.filter(client=request.user.id)
    requested_metric = request.POST['metric']
    data = []
    for q in qs:
        try:
            metric = Metric.objects.get(group=q.id,
                                        name=requested_metric)
            group = model_to_dict(q)
            group['metrics'] = [
                {'x': 1, 'y': metric.lowest},
                {'x': 2, 'y': metric.lower},
                {'x': 3, 'y': metric.average},
                {'x': 4, 'y': metric.higher},
                {'x': 5, 'y': metric.highest}
            ]
            data.append(group)
        except Metric.DoesNotExist:
            pass
    return HttpResponse(json.dumps(data), content_type="application/json")
