from django.shortcuts import render

from django.http import Http404
from django.shortcuts import get_object_or_404
from BackEnd.models import Group,ClassroomIntroducts,Course,DownLoadFiles


def DBprocess(dbtype):
    switch_db = {"classroom":Course,"ClassroomIntroducts":ClassroomIntroducts}
    return switch_db.get(dbtype)

def index(request):
    return render(request, "FrontEnd/index/index.html")

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

def downloadFile(request, getid):
    x = DownLoadFiles.objects.get(id=getid)

    with open(x.filepath.path, 'rb') as fh:
        print(x.filepath.path)
        # response = HttpResponse(fh.read())
        # response['Content-Type'] = 'application/octet-stream'
        # response["Content-Disposition"] = "attachment; filename*=UTF-8''{}".format(os.path.basename(file_path))
        # return response
    raise Http404
def courselist(request):
    
    return render(request, "FrontEnd/course/course_list.html")


def basesingle(request,dbtype,id):
    getdb = DBprocess(dbtype)
    data={}
    if getdb ==None:
        print("error")
    else:
        
        data["data"]=get_object_or_404(getdb,id=id)
    # print(data["showdata"])
    # if(dbtype=="classroom")
    
    return render(request, "FrontEnd/base_single/base_single.html",data)

def classshow(request,id):
    data = Group.objects.get(id=id)
    datatitle="課程教室 /"
    context = {
        'data': data,
        'datatitle': datatitle,
    }

    return render(request, "Frontend/base_single/base_single.html", context)