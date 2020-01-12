from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'gallery'

urlpatterns = [
    url(r'^/$', views, name='home'),
    url(r'^()/$')
]