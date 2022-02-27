from calendar import c
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "FrontEnd/index/index.html")


def single(request):
    return render(request, "FrontEnd/base_single/base_single.html")
def courselist(request):
    x = dict()
    x["date"] = "23"
    x["type"] = "213"
    template = get_template("FrontEnd/course/classroom_box.html")
    html = template.render({"data": x})
    print(html)
    return render(request, "FrontEnd/course/course_list.html")
