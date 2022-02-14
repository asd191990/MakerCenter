from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import NewsForm
from .models import News
from django.views.decorators.csrf import csrf_exempt

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