from django.urls import path

from catalog import views

# Так называемая система роутинга, которая отвечает за то
# какая функция будет выполяеться при обращении на определенный url
urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('json/<int:page>/<str:search_query>/<str:order_by>/', views.api_catalog, name='json_catalog')
]