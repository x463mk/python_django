# Generated by Django 2.2 on 2022-05-11 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertisementAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertisementStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=1000, verbose_name='Заголовок')),
                ('description', models.CharField(default='', max_length=1000, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('closed_at', models.DateTimeField(auto_now=True, verbose_name='Дата окончания публикации.')),
                ('price', models.FloatField(default=0, verbose_name='цена')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
                ('author', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.AdvertisementAuthor', verbose_name='Автор')),
                ('categories', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.AdvertisementCategories', verbose_name='Категории')),
                ('status', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertisements', to='ads.AdvertisementStatus', verbose_name='Статус')),
            ],
            options={
                'db_table': 'ads_advertisement',
                'ordering': ['title'],
            },
        ),
    ]
