from django.shortcuts import render


def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')