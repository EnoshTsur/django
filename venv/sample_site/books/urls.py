from django.conf.urls import url
from django.urls import path
from .views import index , genre, get_book, by_id, get_params

urlpatterns = [
    url(r'^$', index),
    url(r'^genre', genre),
    path('get_book/<int:index>', get_book),
    url(r'^by_id/(?P<index>[1-70]+)$', by_id),
    url(r'^params/', get_params)

]