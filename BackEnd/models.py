import imp
from importlib.resources import contents
from turtle import update
from django.db import models
from django.utils import timezone
# django-ckeditor
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from itertools import chain

# 最新消息

class News(models.Model):
    News_type = (
        ('1', '最新消息'),
        ('2', '學生活動'),
        ('3', '學術動態'),
    )
    title = models.CharField(max_length=30, verbose_name="標題")
    content = RichTextUploadingField(verbose_name='編輯器內文' ,blank=True, null=True)
    type = models.CharField(max_length=1, choices=News_type)
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "最新公告"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.title
    def to_dict(instance):
        opts = instance._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data


# 課程(專業、核心)

class Course(models.Model):
    Courese_type = (
        ('1', '專業'),
        ('2', '核心'),
        ('3', '微學分課程及工作坊'),
    )
    title = models.CharField(max_length=30, verbose_name='課程名稱')
    content = RichTextUploadingField(verbose_name='課程內容',blank=True, null=True)
    type = models.CharField(max_length=1, choices=Courese_type)
    image = models.ImageField(upload_to="courseimage", verbose_name='封面圖')
    created_date = models.DateField(default=timezone.now, verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "課程"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.title
    def to_dict(instance):
        opts = instance._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data


#空間介紹 - 校級共用實驗室借用情形

class ClassroomIntroducts(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    imageone = models.ImageField(upload_to="classimage")
    # 可能有照片要加 但先這樣
    class Meta:
        verbose_name = "教室借用情形"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.title
    def to_dict(instance):
        opts = instance._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data


# 各類申請及說明 / 相關辦法

class DownLoadFiles(models.Model):
    DownLoadFiles_type = (
        ('1', '專業領域小組'),
        ('2', '課程'),
        ('3', '設備及物品借用'),
        ('4', 'TA實習申請'),
    )
    title = models.CharField(max_length=30)
    type = models.CharField(max_length=1, choices=DownLoadFiles_type, null=True)
    content = models.TextField(verbose_name='說明')
    filepath = models.FileField(upload_to='uploads')
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "相關辦法"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.title
    def to_dict(instance):
        opts = instance._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data


# 成員

class Memebers(models.Model):
    name = models.CharField(max_length=30, verbose_name='姓名')
    extension = models.CharField(verbose_name='分機',max_length=20)
    email = models.EmailField(max_length=30,unique=True, verbose_name='電子信箱')
    work = models.TextField(verbose_name='業務職掌')
    location = models.TextField(verbose_name='位置')
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "成員"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.name
    def to_dict(instance):
        opts = instance._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data


# 專業領域小組

class Group(models.Model):
    Group_type = (
        ('1', '智慧製造'),
        ('2', '資訊通'),
        ('3', '機器人'),
        ('4', '創課'),
        ('5', '元宇宙'),
    )
    title = models.CharField(max_length=30, verbose_name='標題',null=True)
    content = RichTextUploadingField(blank=True,null=True)
    type = models.CharField(max_length=1, choices=Group_type, null=True)
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "專業領域小組"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.title
    def to_dict(instance):
        opts = instance._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data


# 空間介紹

class Space(models.Model):
    code = models.CharField(max_length=4,verbose_name='教室代碼')
    name = models.CharField(max_length=30,verbose_name='教室名稱')
    space_description = models.TextField(verbose_name='空間介紹')
    number = models.CharField(max_length=30,verbose_name='容納人數')
    equipment_description = models.CharField(max_length=30,verbose_name='設備資訊')
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "空間介紹"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.name
    def to_dict(instance):
        opts = instance._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data

# 設備介紹

class Equipment(models.Model):
    name = models.CharField(max_length=30,verbose_name='設備名稱')
    description = models.TextField(verbose_name='設備介紹')
    created_date = models.DateField(default=timezone.now,verbose_name='建立日期')
    update_date = models.DateField(auto_now=True, verbose_name='更新日期')
    class Meta:
        verbose_name = "設備介紹"   # 單數
        verbose_name_plural = verbose_name   #複數
    def __str__(self):
        return self.name
    def to_dict(instance):
        opts = instance._meta
        data ={}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data
