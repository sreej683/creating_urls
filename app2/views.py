from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse

def lasya(request):
    return HttpResponse("<h1><marquee>lasya is a good girl</marquee></h1>")


 
