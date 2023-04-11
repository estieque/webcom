from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError

def custom_400_view(request, exception):
    return HttpResponseBadRequest(render(request, '400.html'))

def custom_403_view(request, exception):
    return HttpResponseForbidden(render(request, '403.html'))

def custom_404_view(request, exception):
    return HttpResponseNotFound(render(request, '404.html'))

def custom_500_view(request):
    return HttpResponseServerError(render(request, '500.html'))
