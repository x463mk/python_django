# Generated by Django 2.2 on 2022-06-12 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blogs', '0002_auto_20220611_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.PositiveIntegerField(default=0, verbose_name='лайки'),
        ),
    ]
