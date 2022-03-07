
from django.urls import path, re_path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('base_single/', views.basesingle, name='base_single'),
    path('course-page/', views.coursepage, name='course-page'),
    # 位置
    path('position/', views.position, name='position'),
    # 最新公告
    path('news_list/', views.newslist, name='news_list'),
    # 空間介紹
    path('space_intro/', views.spaceintro, name='space_intro'),
    path('course_list/', views.courselist, name='course_list'),
    path('single/<str:dbtype>', views.single, name='single'),
    # 設備介紹
    path('equipment_intro/', views.equipmentintro, name='equipment_intro'),
    # 成員
    path('members_intro/', views.membersintro, name='members_intro'),
    # 相關辦法
    path('download/', views.download, name='download'),
]
