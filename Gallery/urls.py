from django.urls import re_path,path
from django.conf.urls import url
from . import views

app_name = 'gallery'

urlpatterns = [

    re_path(r'^$', views.IndexView.as_view(), name='home'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='album-display'),
    url(r'^logout/$', views.signout, name='sign-out'),
    re_path(r'^create/$', views.create, name='create-album'),
    re_path(r'^(?P<pk>[0-9]+)/upload/$', views.upload, name='upload-image'),

    # #Starring albums
    re_path(r'^(?P<pk>[0-9]+)/toggle/$', views.toggleFavourite, name='toggle-favourite'),

    # #Delete album
    re_path(r'^(?P<pk>[0-9]+)/delete-album/$', views.deleteAlbum, name='delete-album'),
    #
    # # Starring pics
    # re_path(r'^(?P<album_id>[0-9]{4}/star-pic)/$', views, name='star-pic'),
    # re_path(r'^(?P<album_id>[0-9]{4}/unstar-pic)/$', views, name='unstar-pic'),
    #
    # # Delete pics
    re_path(r'^(?P<pk>[0-9]+)/delete-pic/$', views.deleteImage, name='delete-pic'),

]