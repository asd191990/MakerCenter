from django.shortcuts import render

from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from BackEnd.models import Group,ClassroomIntroducts,Course,DownLoadFiles
from BackEnd.fuc import DBprocess
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import StreamingHttpResponse,FileResponse

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
  
# 相關辦法 -> 下載檔案
def downloadFile(request, getid):
    getfile = get_object_or_404(DownLoadFiles, id=getid)
    usepath=getfile.filepath.path   
    the_file_name  =os.path.basename(usepath)
    readfile = open(usepath, 'rb')
    response = StreamingHttpResponse(readfile)
    response['Content-Type'] = 'application/octet-stream'
    response["Content-Disposition"] = f'attachment; filename="{the_file_name}"'
    return response

    # return render(request, "FrontEnd/index/index.html")

def courselist(request):
    return render(request, "FrontEnd/course/course_list.html")

def basesingle(request,dbtype,id):
    getdb = DBprocess(dbtype)
    data={}
    if getdb ==None:
        print("error")
    else:
        data["data"]=get_object_or_404(getdb,id=id)
    return render(request, "FrontEnd/base_single/base_single.html",data)

def classshow(request,id):
    data = Group.objects.get(id=id)
    datatitle="課程教室 /"
    context = {
        'data': data,
        'datatitle': datatitle,
    }
    return render(request, "Frontend/base_single/base_single.html", context)