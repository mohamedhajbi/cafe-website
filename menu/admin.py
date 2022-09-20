from django.contrib import admin
from . import models

class CategoriesAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(models.Categories,CategoriesAdmin)

class ListAdmin(admin.ModelAdmin):
    list_display=('name','categories','prix')
admin.site.register(models.List,ListAdmin)