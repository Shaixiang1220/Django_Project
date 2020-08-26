from django.contrib import admin
from .models import *

#修改title和header
admin.site.site_title = '信息反馈后台系统'
admin.site.site_header = '信息反馈平台'

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'timestamp']
    search_fields = ['name']
    list_filter = ['name']
    ordering = ['id']
    date_hierarchy = 'timestamp'