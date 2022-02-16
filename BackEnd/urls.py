
from django.urls import path, re_path

from . import views

from django.contrib.admin.views.decorators import staff_member_required


urlpatterns = [
    # path('ckeditor/upload/', staff_member_required(ckeditor_views.upload), name='ckeditor_upload'),
    # 拿掉 staff_member_required()
    # 上傳需要有url地址
    path('ckeditor/upload/', views.Index, name='ckeditor_upload'),

    path('newsmanage/', views.NewsManage, name='NewsManage'),
    # path('newsupdate/', views.NewsUpdate, name='NewsUpdate'),
    path('newsupdate/<int:id>', views.NewsUpdate, name='NewsUpdate'),
    path('news_show/<int:id>', views.NewsShow, name='NewsShow'),
    path('', views.Index, name='Index'),
]
