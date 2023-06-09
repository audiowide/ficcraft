# Generated by Django 4.2 on 2023-05-28 13:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fanfic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, default='', upload_to='profile/avatars')),
                ('background', models.FileField(blank=True, default='', upload_to='profile/background-image/')),
                ('about', models.TextField(blank=True)),
                ('coins', models.IntegerField(default=0)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('bookmarks', models.ManyToManyField(default=[], to='fanfic.chapter')),
                ('lowers', models.ManyToManyField(default=[], to='fanfic.work')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('works', models.ManyToManyField(default=[], to='fanfic.work')),
            ],
        ),
    ]
