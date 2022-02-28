from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from .forms import NewsForm
from .models import News,Course
from .filters import NewsFilter

#新增消息

def Index(request):

    user = News.objects.all()

    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("")
        else:
            print(form.errors)
            
    context = {
        'user': user,
        'form': form
    }

    return render(request, "BackEnd/index/index.html", context)

#消息管理及查詢

def NewsManage(request):

    news = News.objects.all()

    newsFilter = NewsFilter(queryset=news)

    if request.method == "POST":
        newsFilter = NewsFilter(request.POST, queryset=news)

    form = NewsForm()

    context = {
        'news': news,
        'form': form,
        'newsFilter': newsFilter
    }
    
    return render(request, "BackEnd/news_manage.html", context)

# 更新消息

def NewsUpdate(request,id):
    news = News.objects.get(id=id)
    
    form = NewsForm(instance=news)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/' + id)

    context = {
        'news': news,
        'form': form
    }

    return render(request, "BackEnd/news_update.html", context)

def NewsShow(request,id):
    news = News.objects.get(id=id)
    

    context = {
        'news': news,
    }

    return render(request, "BackEnd/news_show.html", context)


def DBlist(request,dbtype):
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

    data = {
        "datalist": datalist
    }
    return JsonResponse(data)