from django.contrib import admin

from catalog.models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'datetime', 'image')


admin.site.register(Products, ProductsAdmin)
