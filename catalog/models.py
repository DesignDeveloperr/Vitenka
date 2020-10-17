from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    datetime = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'