
from django.urls import path, re_path

from . import views

from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    path('', views.Index, name='Index'),
    # path('ckeditor/upload/', staff_member_required(ckeditor_views.upload), name='ckeditor_upload'),
    re_path(r'^ckeditor/upload/', staff_member_required(views.Index), name='ckeditor_upload'),
]
