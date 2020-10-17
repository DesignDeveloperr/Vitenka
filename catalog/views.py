from django.shortcuts import render


def catalog(request):
    if request.method == 'GET':
        return render(request, 'catalog.html')