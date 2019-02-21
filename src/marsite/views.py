from django.shortcuts import render


def not_found_view(req):
    return render(req, '404.html')
