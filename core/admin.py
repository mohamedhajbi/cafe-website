from django.contrib import admin
from . import models



class BookAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.Book,BookAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display=('user','post','date')
admin.site.register(models.Comment,CommentAdmin)

class EventsImageAdmin(admin.ModelAdmin):
    list_display=('title','image_tag')
admin.site.register(models.EventsImage,EventsImageAdmin)
