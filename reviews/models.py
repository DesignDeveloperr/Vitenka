from django.db import models


class Reviews(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    text = models.TextField(verbose_name='Текст')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
