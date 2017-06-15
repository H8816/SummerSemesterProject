from django.conf.urls import url
from . import views

app_name = 'app'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name="register"),
    url(r'^threads/$', views.threads, name='threads'),
    url(r'^music/$', views.music, name='music'),
    url(r'^currency/$', views.currency, name='currency'),
    url(r'^threads/(?P<thread_id>[0-9]+)$', views.detailed_view, name='detailed_view'),
    url(r'^movies/$', views.movies, name='movies'),
    url(r'^love/$', views.love, name='love'),
    url(r'^education/$', views.education, name='education'),
    url(r'^development/$', views.development, name='development'),
    url(r'^newthread/$', views.newThread, name='newThread'),
]
