from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewsForm
from .models import News
from django.views.decorators.csrf import csrf_exempt

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

    return render(request, "index.html", context)

#消息管理

def NewsManage(request):

    news = News.objects.all()

    form = NewsForm()

    context = {
        'news': news,
        'form': form
    }
    
    return render(request, "news_manage.html", context)

# 更新消息

def NewsUpdate(request, pk):

    news = News.objects.get(id=pk)
    
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

    return render(request, "news_update.html", context)