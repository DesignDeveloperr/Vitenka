from django.shortcuts import render

from catalog.services import get_json_catalog, get_catalog_pages


# Вывод HTML шаблона
def catalog(request):
    if request.method == 'GET':
        return render(request, 'catalog.html')


# Вывод JSON массива с товарами для JS
def api_catalog(request, page, search_query, order_by):
    if request.method == 'GET':
        return get_json_catalog(page, search_query, order_by)


# JSON массив с кол-вом страниц для каталога
def api_catalog_pages(request):
    if request.method == 'GET':
        return get_catalog_pages()
