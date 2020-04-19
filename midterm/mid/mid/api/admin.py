from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from mid.api.models import Book,Journal


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'description', 'num_pages', 'genre', 'created_at')


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('id', 'price', 'description', 'publisher', 'type', 'created_at')

