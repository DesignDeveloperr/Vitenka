import math

from django.http import JsonResponse
from django.utils import formats

from catalog.models import Products


# Структура приложений джанги говорит, что бизнес-логику надо писать во views,
# но как показывает практика - лучше разделять отображение шаблонов и логику
def get_json_catalog(page: int, search_query: str, order_by: str) -> object:
    # Получаем все продукты из базы
    products = Products.objects.all()

    # Если заданы параметры, то фильтруем
    if not search_query == 'all':
        products = products.filter(name__iregex=search_query)
    if not order_by == 'none':
        products = products.order_by(order_by)
    products = products[(page * 6) - 6: page * 6]

    # Создаем пустой массив и через цикл заполняем его оставщимся продуктами после фильтрации
    # в нужном форамате для JSON ответа
    data = []
    for i in products:
        data += [{
            'name': i.name,
            'price': str(i.price) + ' руб.',
            'date': formats.date_format(i.datetime, "SHORT_DATETIME_FORMAT"),
            'image': i.image.url
        }]

    # Отдаем на страницу готовый JSON масссив для JavaScript
    return JsonResponse(data, safe=False)


# Получаем кол-во старниц для каталога
def get_catalog_pages() -> object:
    data = []
    for i in range(math.ceil(Products.objects.count() / 6)):
        data.append(i + 1)
    return JsonResponse(data, safe=False)
