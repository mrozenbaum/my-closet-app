from django.conf.urls import url

from . import views

app_name = 'closetclient'
urlpatterns = [
    # ex: /closetclient/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # ex: /closetclient/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /closetclient/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /closetclient/5/vote/
    url(r'^(?P<category_id>[0-9]+)/item_count/$', views.item_count, name='item_count'),
]