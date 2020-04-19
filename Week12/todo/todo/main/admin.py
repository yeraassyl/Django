from django.contrib import admin

from todo.main.models import ToDoList, ToDo


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id','name','img','owner')


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'list', 'created_at', 'is_done', )