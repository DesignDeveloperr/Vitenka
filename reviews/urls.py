from django.urls import path
from reviews import views
from reviews.views import api_reviews

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('json/', api_reviews, name='json_reviews')
]