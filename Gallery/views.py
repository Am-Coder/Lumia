from django.shortcuts import render,get_object_or_404,redirect
from django.views import generic
from .models import *
from . import form
from django.urls import reverse
from django.views.generic import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'all_albums'
    paginate_by = 10

    def get_queryset(self):
        return Album.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = form.AlbumForm
        return context


class AlbumDetailView(generic.DetailView):
    model = Album
    context_object_name = 'album'
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form1'] = form.ImageForm
        context['form'] = form.AlbumForm
        return context


@login_required
def logout_view(request):
    logout(request)


@login_required
def create(request):
    if request.method == 'POST':
        myform = form.AlbumForm(request.POST, request.FILES)
        if myform.is_valid():
            data = myform.cleaned_data
            album = Album()
            album.user_id = request.user
            album.album_starred = data['album_starred']
            album.album_name = data['album_name']
            album.album_logo = data['album_logo']
            album.album_short_des = data['album_short_des']
            album.save()
            return redirect(album.get_absolute_url())

    return redirect(reverse("gallery:home"))


@login_required
def upload(request,pk):
    if request.method == 'POST':
        # print(pk + request.POST.get('image_short_des'))
        myform = form.ImageForm(request.POST, request.FILES)
        if myform.is_valid():
            data = myform.cleaned_data
            image = Image()
            image.album_id = Album.objects.get(album_id =pk)
            image.image_starred = data['image_starred']
            image.image_short_des = data['image_short_des']
            image.image_file = data['image_file']
            image.save()
            return redirect(image.get_absolute_url())
        print(myform.errors)
    return redirect(reverse("gallery:home"))


@login_required
def deleteAlbum(request,pk):
    print(pk)
    Album.objects.get(album_id=pk).delete()
    return redirect(reverse("gallery:home"))


@login_required
def deleteImage(request,pk):
    image = Image.objects.get(image_id=pk)
    urlred = image.get_absolute_url()
    image.delete()
    return redirect(urlred)


@login_required
def toggleFavourite(request, pk):
    album = Album.objects.get(album_id=pk)
    album.album_starred = not album.album_starred
    album.save()
    return JsonResponse({'status': album.album_starred})