from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def yash(request):
    return HttpResponse('<h1><marquee>yash is handsome</marquee></h1>')