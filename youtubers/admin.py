from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html

class YTAdmin(admin.ModelAdmin):
    def display_photo(self, object):
        return format_html("<img src='{}' width='60' />".format(object.photo.url))

    list_display = ('id', 'display_photo', 'name', 'subs_count', 'is_featured')
    search_fields = ('name', 'camera_type')
    list_filter = ('city', 'camera_type')
    list_display_links = ('id', 'name',)
    list_editable = ('is_featured',)
admin.site.register(Youtuber, YTAdmin)