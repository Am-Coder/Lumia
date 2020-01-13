from django.shortcuts import render,get_object_or_404
from django.views import generic
from .models import *
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class AlbumDetailView(generic.DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'gallery.html'
