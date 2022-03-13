from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import NewsForm
from .models import News,Course,Group,DownLoadFiles
from .filters import NewsFilter



def DBlist(request,dbtype):
    datalist=[]
    if dbtype=="download":
        getlist = DownLoadFiles.objects.all()
        for v in getlist:
            v =  v.__dict__
            del v['_state']
            datalist.append(v)
        print(datalist)

    else:
        print(dbtype)
        
        getlist = Course.objects.all()
        print(getlist)
        print(getlist[0].__dict__)
        datalist = []
        for v in getlist:
            v.type = v.get_type_display()
            v =  v.__dict__
            del v['_state']
            datalist.append(v)
        print(datalist)
    return JsonResponse(datalist,safe=False)