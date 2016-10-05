from django.contrib import admin

from .models import News
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'image1', 'status', 'publish', 'created']
    search_fields = ('title', 'body')
    list_filter = ['title']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    list_per_page = 10

    class Meta:
        model = News


admin.site.register(News, NewsAdmin)

