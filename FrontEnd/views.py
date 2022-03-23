from django.shortcuts import render

from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from BackEnd.models import Group,ClassroomIntroducts,Course,DownLoadFiles,News
from BackEnd.fuc import DBprocess
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import StreamingHttpResponse
from django.core.paginator import Paginator

def index(request):
    news = News.objects.all()
    # 顯示三筆資料
    paginator = Paginator(news, 3)
    # 獲取url中的頁碼，比如第一頁，我們需要在url末尾中新增 ?page=1
    page = request.GET.get('page')
    # 獲取相應的頁碼的資料，比如page=1，第一頁，這裡獲取得到第一頁的資料內容
    news = paginator.get_page(page)
    # 獲取一共分出來了多少頁，前端展示所有頁碼數的時候需要用到該數
    print("總共有",paginator.num_pages,"頁")
    print("多少資料",paginator.object_list)
    print(news.paginator.page_range)

    context = {
        'news': news
    }
    return render(request, "FrontEnd/index/index.html",context)

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
def courselist_gettype(request, type):
    print("得到的type")
    print(type)
    context = {
        'coursetype':type
    }
    return render(request, "FrontEnd/course/course_list.html",context)

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