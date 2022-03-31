
# from django.conf import settings
# from django.views.static import serve

from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('media/', serve,{'document_root': settings.MEDIA_ROOT}),
    # path('static/', serve,{'document_root': settings.STATIC_ROOT}),
    path('', views.index, name='index'),
    path('course-page/', views.coursepage, name='course-page'),
    path('position/', views.position, name='position'),
    path('news_list/', views.newslist, name='news_list'),
    path('space_intro/', views.spaceintro, name='space_intro'),
    path('course_list/', views.courselist, name='course_list'),
    path('course_list/<str:type>', views.courselist_gettype, name='courselist_gettype'),
    
    path('equipment_intro/', views.equipmentintro, name='equipment_intro'),
    path('members_intro/', views.membersintro, name='members_intro'),
    path('download/', views.download, name='download'),
    # 相關辦法 下載
    path('download/<int:getid>',views.downloadFile, name='download_file'),
    #分頁
    path('single/<str:dbtype>/<int:id>', views.basesingle, name='thesingle'),
    #專業小組
    path('class/<int:id>', views.classshow, name='classshow'),
]
