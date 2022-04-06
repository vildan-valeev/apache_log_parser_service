from django.contrib import admin

from .models import Log, TestLog, LogFile


class LogAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'ip', ]
    list_display = ['id', 'ip', 'url', 'method', 'code']
    list_filter = ['ip', 'method', 'code']


class TestLogAdmin(admin.ModelAdmin):
    list_display_links = ['id', ]
    list_display = ['id', 'row']


class LogFileAdmin(admin.ModelAdmin):
    list_display_links = ['id', ]
    list_display = ['id', 'file', 'processed']
    readonly_fields = ['processed']


admin.site.register(TestLog, TestLogAdmin)

admin.site.register(Log, LogAdmin)
admin.site.register(LogFile, LogFileAdmin)
