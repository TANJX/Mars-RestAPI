import json
from django.http import HttpResponse, HttpResponseRedirect
from .url_sign import sign_url


def maps(req):
    response = {}
    if req.method == "POST":
        post = req.POST
        if 'url' not in post:
            response['error'] = 'Missing url variable'
        else:
            result = sign_url(post['url'])
            return HttpResponse(result)
    else:
        response['status'] = 'error'
        response['msg'] = 'Not a POST request'
    return HttpResponse(json.dumps(response))
