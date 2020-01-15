from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



def upload_file_directory(instance, filename):
    return 'user_{0}/{1}'.format(instance.user_id, filename)

def upload_image_directory(instance, filename):
    return 'user_{0}/{1}'.format(instance.album_id.user_id, filename)

# Create your models here.
class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    album_starred = models.BooleanField(default=False)
    album_short_des = models.CharField(max_length=100, null = True)
    album_logo = models.FileField(null=True, upload_to=upload_file_directory)
    album_name = models.CharField(max_length=50, default='My Album')

    def get_absolute_url(self):
        return reverse("gallery:album-display", kwargs={'pk': self.pk})

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    image_starred = models.BooleanField(default=False)
    image_short_des = models.CharField(max_length=50, null=True)
    image_file = models.FileField(null=True, upload_to=upload_image_directory)

    def get_absolute_url(self):
        return reverse("gallery:album-display", kwargs={'pk': self.album_id.album_id})


