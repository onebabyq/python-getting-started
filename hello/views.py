from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def line(request):
    # return HttpResponse('Line!')
    return render(request, "line.html")
def dataanalysys(request):
    # return HttpResponse('Dataanalysys!')
    return render(request, "dataanalysys.html")
def scatter(request):
    # return HttpResponse('Line!')
    return render(request, "scatter.html")
def simplechart(request):
    # return HttpResponse('Line!')
    return render(request, "simplechart.html")
def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
