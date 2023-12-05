from django.contrib import admin
from adding_list.models import addList
# Register your models here.
class addListAdmin(admin.ModelAdmin):
    list_display = ['name','marks']
admin.site.register(addList,addListAdmin)