from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    return render(request, "FrontEnd/index/index.html")


def single(request):
    return render(request, "FrontEnd/base_single/base_single.html")
