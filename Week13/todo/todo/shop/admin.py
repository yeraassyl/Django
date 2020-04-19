from django.contrib import admin

from todo.shop.models import Category, OnlineProduct


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','created_at', 'created_by')


@admin.register(OnlineProduct)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',  'created_at', 'price', )