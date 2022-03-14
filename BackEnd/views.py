from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import NewsForm
from .models import News,Course,Group,DownLoadFiles,Memebers,Equipment,Space
from .filters import NewsFilter

from .fuc import DBprocess


def DBlist(request,dbtype):
    datalist=[]
    if dbtype=="DownLoadFiles":
        getlist = DownLoadFiles.objects.all()
        for v in getlist:
            v.typeshow = v.get_type_display()
            v =  v.__dict__        
            del v['_state']
            del v['filepath']
            del v['_django_cleanup_original_cache']
            datalist.append(v)
        print(datalist)
    
    elif   dbtype=="Memebers":
        getlist = Memebers.objects.all()
        for v in getlist:
            v =  v.__dict__
            del v['_state']
            datalist.append(v)
        print(datalist)
    
    elif   dbtype=="News":
        getlist = News.objects.all()
        for v in getlist:
            v =  v.__dict__
            del v['_state']
            datalist.append(v)
        print(datalist)
    elif   dbtype=="Equipment":
        getlist = Equipment.objects.all()
        for v in getlist:
            v =  v.__dict__
            del v['_state']
            datalist.append(v)
        print(datalist)
    elif   dbtype=="Space":
        getlist = Space.objects.all()
        for v in getlist:
            v =  v.__dict__
            del v['_state']
            datalist.append(v)
        print(datalist)

    else:
        print(dbtype)
        
        getlist = Course.objects.all()
        print(getlist)
        datalist = []
        for v in getlist:
            v.typeshow = v.get_type_display()
            v =  v.__dict__
            del v['_state']
            del v['image']
            del v['_django_cleanup_original_cache']
            datalist.append(v)
        print(datalist)
    return JsonResponse(datalist,safe=False)