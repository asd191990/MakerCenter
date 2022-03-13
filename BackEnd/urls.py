
from django.urls import path, re_path

from . import views

from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('getlist/<str:dbtype>', views.DBlist, name='apigetdblist'),
]
