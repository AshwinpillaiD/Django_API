from django.shortcuts import render

from django.http import JsonResponse
# Create your views here.


def blog (request):
    data={
        "Name" : "Ashwin"
    }
    return JsonResponse(data)