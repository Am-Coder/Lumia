from django.contrib import admin
from Gallery.models import Album,Image
# Register your models here.
admin.site.register([Album, Image])