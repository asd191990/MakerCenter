from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "FrontEnd/index/index.html")
def basesingle(request):
    return render(request, "FrontEnd/base_single/base_single.html")
def coursepage(request):
    return render(request, "FrontEnd/course-page/course-page.html")
def position(request):
    return render(request, "FrontEnd/position/position.html")
def newslist(request):
    return render(request, "FrontEnd/news_list/news_list.html")
def spaceintro(request):
    return render(request, "FrontEnd/space_intro/space_intro.html")
def equipmentintro(request):
    return render(request, "FrontEnd/equipment_intro/equipment_intro.html")
def membersintro(request):
    return render(request, "FrontEnd/members_intro/members_intro.html")
def download(request):
    return render(request, "FrontEnd/download/download.html")

def single(request):
    return render(request, "FrontEnd/base_single/base_single.html")
def courselist(request):
    
    return render(request, "FrontEnd/course/course_list.html")
