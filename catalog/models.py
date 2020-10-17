from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    image = models.ImageField(upload_to='products', verbose_name='Лого')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'