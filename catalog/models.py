from django.db import models


# Создаем модель (таблицу) с продуктами, настраиваем поля в таблице
class Products(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(upload_to='products', verbose_name='Лого')

    # Отвечает за отображение заголовка строк в таблице в админ-панеле
    def __str__(self):
        return self.name

    # Чеолевеческое название в ед.ч и в мн. ч.
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'