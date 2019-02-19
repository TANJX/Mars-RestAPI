import json
from django.http import HttpResponse, HttpResponseRedirect
from .ping_server import StatusPing


def info(req):
    response = {}
    if req.method == "GET":
        get = req.GET
        if 'server' not in get:
            response['error'] = 'Missing server variable'
        else:
            result = StatusPing(get['server']).get_status()
            return HttpResponse(json.dumps(result))
    else:
        response['error'] = 'Not a GET request'
    return HttpResponse(json.dumps(response))
