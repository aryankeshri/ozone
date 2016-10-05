from django.contrib import admin
from embed_video.admin import AdminVideoMixin
# Register your models here.

from  .models import Join, PhotoDay, Event, Ofctv

class JoinAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'city', 'contact']
    list_per_page = 10
    search_fields = ['name']

    class Meta:
        model = Join

class PhotoDayAdmin(admin.ModelAdmin):
    list_display = ['id', 'image1', 'title', 'status']
    list_editable = ['title', 'status']
    list_per_page = 10

    class Meta:
        model = PhotoDay

class EventAdmin(admin.ModelAdmin):
    list_display = ['image1', 'title', 'status']
    list_editable = ['title', 'status']
    list_per_page = 10

    class Meta:
        model = Event

class OfctvAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ['video', 'title', 'created', 'type']
    list_per_page = 10

    class Meta:
        model = Ofctv
        ordering = ('-created',)




admin.site.register(Ofctv, OfctvAdmin)
admin.site.register(PhotoDay, PhotoDayAdmin)
admin.site.register(Join, JoinAdmin)
admin.site.register(Event, EventAdmin)

