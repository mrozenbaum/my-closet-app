from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /closetclient/
    url(r'^$', views.index, name='index'),
    # ex: /closetclient/5/
    url(r'^(?P<category_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /closetclient/5/results/
    url(r'^(?P<category_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /closetclient/5/vote/
    url(r'^(?P<category_id>[0-9]+)/vote/$', views.item_count, name='vote'),
]