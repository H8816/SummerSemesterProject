from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^threads/$', views.threads, name='threads'),
    url(r'^threads/(?P<thread_id>[0-9]+)$', views.detailed_view, name='detailed_view'),
]
