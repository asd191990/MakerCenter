
from django.urls import path, re_path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('base_single/', views.basesingle, name='base_single'),
    path('course-page/', views.coursepage, name='course-page'),
    path('position/', views.position, name='position'),
    path('news_list/', views.newslist, name='news_list'),
    path('space_intro/', views.spaceintro, name='space_intro'),
    path('course_list/', views.courselist, name='course_list'),
    path('single/', views.single, name='single'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)