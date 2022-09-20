from django.contrib import admin
from .models import Room
from . import models



class RoomAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(models.Room,RoomAdmin)

class MessageAdmin(admin.ModelAdmin):
    list_display=('room','user','content','date_added')
admin.site.register(models.Message,MessageAdmin)


