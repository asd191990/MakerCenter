
from django.urls import path, re_path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('course_list', views.courselist, name='course_list'),
    path('single', views.single, name='single'),
]
