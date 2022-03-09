
from django.urls import path, re_path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('course-page/', views.coursepage, name='course-page'),
    path('position/', views.position, name='position'),
    path('news_list/', views.newslist, name='news_list'),
    path('space_intro/', views.spaceintro, name='space_intro'),
    path('course_list/', views.courselist, name='course_list'),
    path('single/', views.single, name='single'),
    path('equipment_intro/', views.equipmentintro, name='equipment_intro'),
    path('members_intro/', views.membersintro, name='members_intro'),
    path('download/', views.download, name='download'),
    #分頁
    path('single/<str:dbtype>/<int:id>', views.basesingle, name='single'),
    #專業小組
    path('class/<int:id>', views.classshow, name='classshow'),
]
