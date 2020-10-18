from django.contrib import admin

from catalog.models import Products


# Настраиваем вывод таблицы в адми-панеле для модели с продуктами
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'datetime', 'image')


# Отображаем модель с продуктими в админ-панеле
admin.site.register(Products, ProductsAdmin)
