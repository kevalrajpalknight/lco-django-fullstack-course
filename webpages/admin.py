from django.contrib import admin
from .models import *
from django.utils.html import format_html

class TeamAdmin(admin.ModelAdmin):
    def display_photo(self, object):
        return format_html("<img src='{}' width='60' />".format(object.photo.url))

    list_display = ('display_photo', 'first_name', 'category')
    search_fields = ('first_name', 'category')

# Register your models here.
admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)