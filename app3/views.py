from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def tamil(request):
    return HttpResponse("<h1><marquee>Tamil is easy to learn</marquee></h1>")