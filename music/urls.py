from django.conf.urls import url
from .views import index, detail, favorite

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', index, name='index'),

    # /music/123/
    url(r'^(?P<album_id>\d+)/$', detail, name='detail'),

    # /music/123/favorite/
    url(r'^(?P<album_id>\d+)/favorite/$', favorite, name='favorite')
]
