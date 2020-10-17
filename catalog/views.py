from django.shortcuts import render

from catalog.services import get_json_catalog


def catalog(request):
    if request.method == 'GET':
        return render(request, 'catalog.html')


def api_catalog(request, page, search_query, order_by):
    if request.method == 'GET':
        return get_json_catalog(page, search_query, order_by)
