from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "FrontEnd/index/index.html")
def courselist(request):
    return render(request, "FrontEnd/course/course_list.html")