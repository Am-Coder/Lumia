from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    album_starred = models.BooleanField(default=False)
    album_short_des = models.CharField(max_length=100, null = True)

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    image_starred = models.BooleanField(default=False)
    image_short_des = models.CharField(max_length=50,null = True)
    image_file = models.FileField()

