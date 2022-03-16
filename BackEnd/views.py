from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import NewsForm
from .models import News,Course,Group,DownLoadFiles,Memebers,Equipment,Space
from .filters import NewsFilter
from django.views.decorators.csrf import csrf_exempt
from .fuc import DBprocess

@csrf_exempt
def DBlist(request,dbtype):
    print(dbtype)
    getdb =DBprocess(dbtype)
    datalist = []
    if dbtype ==None:
        return JsonResponse({"error":"請求失敗"})
    else:        
        getdata = getdb.objects.all()
        for one_data in getdata:
            if getdb != Memebers and getdb != Space and getdb != Equipment:
                # if one_data.get_type_display() != None:
                one_data.type = one_data.get_type_display()
                print(one_data.type)
            data = one_data.to_dict()
            print("-------------------")
            print(data)
            datalist.append(data)
        print(datalist)
    return JsonResponse(datalist, safe=False)
    #     getlist = Course.objects.all()
    #     print(getlist)
    #     datalist = []
    #     for v in getlist:
    #         v.typeshow = v.get_type_display()
    #         v =  v.__dict__
    #         del v['_state']
    #         del v['image']
    #         del v['_django_cleanup_original_cache']
    #         datalist.append(v)
    #     print(datalist)
    # return JsonResponse(datalist,safe=False)

    