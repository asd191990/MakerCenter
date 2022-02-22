import imp
from importlib.resources import contents
from turtle import update
from django.db import models
from django.utils import timezone
# django-ckeditor
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# 最新消息

class News(models.Model):
    title = models.CharField(max_length=30, verbose_name="標題")
    content = RichTextUploadingField(verbose_name='編輯器內文' ,blank=True, null=True)
    date = models.DateField(default=timezone.now,verbose_name='建立日期')
    class Meta:
        verbose_name = "最新公告"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.title




# 課程(專業、核心)

class Coures(models.Model):
    Coure_type = (
        ('1', '專業實作課程'),
        ('2', '核心實作課程'),
    )
    title = models.CharField(max_length=30)
    content = models.TextField()
    type = models.CharField(max_length=1, choices=Coure_type)
    date = models.DateField(default=timezone.now)

# 校級共用實驗室借用情形

class classroomintroducts(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    date = models.DateField(default=timezone.now)
    imageone = models.ImageField(upload_to="classimage")
    # 可能有照片要加 但先這樣

# 各類申請及說明

class DownLoadFiles(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    filepath = models.FileField(upload_to='uploads')
    date = models.DateField(default=timezone.now)
