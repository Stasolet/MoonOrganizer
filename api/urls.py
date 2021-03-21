from django.urls import path

from .views import get_rec, add_rec, moon_news

app_name = 'api'

urlpatterns = {
    path('get_rec/', get_rec, name='get_rec'),
    path('add_rec/', add_rec, name='add_rec'),
    path('moon_news/', moon_news, name='moon_news'),
}
