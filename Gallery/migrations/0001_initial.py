# Generated by Django 2.2.5 on 2020-01-12 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.AutoField(primary_key=True, serialize=False)),
                ('album_starred', models.BooleanField(default=False)),
                ('album_short_descr', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('image_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_starred', models.BooleanField(default=False)),
                ('image_short_des', models.CharField(max_length=50, null=True)),
                ('image_file', models.FileField(upload_to='')),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gallery.Album')),
            ],
        ),
    ]
