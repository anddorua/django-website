from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /music/123/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),

]
