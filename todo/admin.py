from django.contrib import admin
from .models import TodoModel


class TodoModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'text','time', 'is_done','is_urgent']
    search_fields = ['time']

admin.site.register(TodoModel, TodoModelAdmin)
