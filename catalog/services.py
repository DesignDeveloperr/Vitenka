from django.http import JsonResponse
from django.utils import formats

from catalog.models import Products


def get_json_catalog(page: int, search_query: str, order_by: str) -> object:
    products = Products.objects.all()
    if not search_query == 'all':
        products = products.filter(name__iregex=search_query)
    if not order_by == 'none':
        products = products.order_by(order_by)

    data = []
    for i in products[(page * 6) - 6:page * 6 + 6]:
        data += [{
            'name': i.name,
            'price': str(i.price) + 'руб.',
            'date': formats.date_format(i.datetime, "SHORT_DATETIME_FORMAT"),
            'image': i.image.url
        }]

    return JsonResponse(data, safe=False)
