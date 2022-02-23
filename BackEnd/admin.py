from django.contrib import admin
from .models import News, Coures, ClassroomIntroducts, DownLoadFiles, Memebers, Group, Space
# Register your models here.


admin.site.site_header = '大勱客後台管理中心'
admin.site.site_title = '大勱客後台管理中心'
admin.site.index_title = '管理中心'

# 客製化欄位顯示
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'type', 'created_date', 'update_date')
    search_fields = ('title', 'content')
    # list_filter 後面要有 , 
    list_filter = ('update_date',)
    
class CouresAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'type', 'created_date', 'update_date')
class ClassroomIntroductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_date', 'update_date')
class DownLoadFilesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'type', 'created_date', 'update_date')
class MemebersAdmin(admin.ModelAdmin):
    list_display = ('name', 'extension', 'email', 'work', 'location', 'created_date', 'update_date')
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'type', 'created_date', 'update_date')
class SpaceAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'space_description', 'number', 'equipment_description', 'created_date', 'update_date')

# admin要註冊才可以管理這些Table
admin.site.register(News, NewsAdmin)
admin.site.register(Coures, CouresAdmin)
admin.site.register(ClassroomIntroducts, ClassroomIntroductsAdmin)
admin.site.register(DownLoadFiles, DownLoadFilesAdmin)
admin.site.register(Memebers, MemebersAdmin)
admin.site.register(Group, GroupsAdmin)
admin.site.register(Space, SpaceAdmin)
