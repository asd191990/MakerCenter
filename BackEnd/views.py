from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import NewsForm
from .models import News,Course,Group,DownLoadFiles
from .filters import NewsFilter

from .fuc import DBprocess


def DBlist(request,dbtype):
    getdb =DBprocess(dbtype)
    if getdb ==None:
        return JsonResponse({"error":"請求失敗"})
    else:        
        getdata = getdb.objects.all()
        for one_data in getdata:
            data = one_data.to_dict()
            print(data)
        # getdata = getdb.objects.get(id=1).to_dict()


    return JsonResponse(datalist,safe=False)