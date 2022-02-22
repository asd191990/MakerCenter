from django.contrib import admin
from .models import News
# Register your models here.


admin.site.site_header = '大勱客後台管理中心'
admin.site.site_title = '大勱客後台管理中心'
admin.site.index_title = '管理中心'

# 客製化欄位顯示


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')


# admin要註冊才可以管理這些Table
admin.site.register(News, NewsAdmin)
