from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "FrontEnd/index/index.html")
def courselist(request):
    return render(request, "FrontEnd/course/course_list.html")
def basesingle(request):
    return render(request, "FrontEnd/base_single/base_single.html")
def coursepage(request):
    return render(request, "FrontEnd/course_page/course_page.html")
def position(request):
    return render(request, "FrontEnd/position/position.html")
def newslist(request):
    return render(request, "FrontEnd/news_list/news_list.html")
def spaceintro(request):
    return render(request, "FrontEnd/space_intro/space_intro.html")