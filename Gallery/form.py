from django import forms
from Gallery.models import Album, Image


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['album_starred', 'album_name', 'album_short_des', 'album_logo']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_starred', 'image_short_des', 'image_file']