from django.http import HttpResponse
from django.shortcuts import render

def homepage(req):
    # return HttpResponse("Home page")
    return render(req, "homepage.html")

def about(request):
    # return HttpResponse("about")
    return render(request, "about.html")