# Generated by Django 4.2.3 on 2023-07-22 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanfic', '0002_alter_work_image'),
        ('user', '0003_profile_character_bookmarks_profile_fandom_bookmarks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='lowers',
            field=models.ManyToManyField(default=[], related_name='lowered_works', to='fanfic.work'),
        ),
    ]