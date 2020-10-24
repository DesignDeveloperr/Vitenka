from django.shortcuts import render

from reviews.services import add_review, get_json_reviews


def reviews(request):
    # Отображаем HTML шаблон при простом переходе на страницу
    if request.method == 'GET':
        return render(request, 'reviews.html')

    # Выполняем функцию при отправки формы на странице с отзыввми.
    # Можно сделать отдельную функцию и задать для нее url,
    # а можно сделать как вывод так и обработчик одну и ту же страницу разделяя по типу запроса
    if request.method == 'POST':
        return add_review(request)


def api_reviews(request):
    return get_json_reviews()
