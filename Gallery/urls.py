from django.urls import re_path
from django.conf.urls import url
from . import views

app_name = 'gallery'

urlpatterns = [

    re_path(r'^/$', views, name='home'),
    re_path(r'^(?P<album_id>[0-9]{4])/$', views, name='album-display'),
    url(r'^logout/$', views, name='log-out'),
    re_path(r'^create/$', views, name='create-album'),
    re_path(r'^(?P<album_id>[0-9]{4])/upload$', views, name='upload-image'),

    #Starring albums
    re_path(r'^(?P<album_id>[0-9]{4}/star) $', views, name='star'),
    re_path(r'^(?P<album_id>[0-9]{4}/unstar) $', views, name='unstar')

]