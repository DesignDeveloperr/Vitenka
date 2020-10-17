from django.core.serializers import serialize
from django.http import JsonResponse
from django.utils import formats

from reviews.models import Reviews


def add_review(request: object) -> object:
    if not request.POST['name'] == '':
        if not request.POST['text'] == '':
            if len(request.POST['name']) <= 30:
                Reviews.objects.create(
                    name=request.POST['name'],
                    text=request.POST['text']
                )
                return JsonResponse({'type': 'success', 'message': 'Ваш отзыв был добавлен'})
            else:
                return JsonResponse({'type': 'error', 'message': 'Ваше имя слишком длинное'})
        else:
            return JsonResponse({'type': 'error', 'message': 'Заполните поле с текстом'})
    else:
        return JsonResponse({'type': 'error', 'message': 'Заполните поле с именем'})


def get_json_reviews() -> object:
    data = []
    for i in Reviews.objects.all().order_by('-pk'):
        data += [{'name': i.name, 'text': i.text, 'date': formats.date_format(i.datetime, "SHORT_DATETIME_FORMAT")}]
    return JsonResponse(data, safe=False)
