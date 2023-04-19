from django.shortcuts import render
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotFound, HttpResponseServerError

def custom_400_view(request, exception):
    return render(request, '400.html')

def custom_403_view(request, exception):
    return render(request, '403.html')

def custom_404_view(request, exception):
    return render(request, '404.html')

def custom_500_view(request):
    return render(request, '500.html')
