
from django.urls import path, re_path

from . import views

from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    #ckeditor 上傳專用url地址
    path('ckeditor/upload/', views.Index, name='ckeditor_upload'),
    path('newsmanage/', views.NewsManage, name='NewsManage'),
    path('newsupdate/<int:id>', views.NewsUpdate, name='NewsUpdate'),
    path('newsshow/<int:id>', views.NewsShow, name='NewsShow'),

    #corrout
    path('list/<str:dbtype>', views.DBlist, name='manage'),
    path('', views.Index, name='Index'),
]
