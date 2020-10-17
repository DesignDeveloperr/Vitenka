from django.shortcuts import render

from reviews.services import add_review, get_json_reviews


def reviews(request):
    if request.method == 'GET':
        return render(request, 'reviews.html')

    if request.method == 'POST':
        return add_review(request)


def api_reviews(request):
    if request.method == 'GET':
        return get_json_reviews()
