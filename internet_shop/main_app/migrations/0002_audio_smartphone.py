# Generated by Django 3.2 on 2021-04-07 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('diagonal', models.CharField(max_length=250, verbose_name='Размер экрана')),
                ('memory', models.CharField(max_length=250, verbose_name='Встроенная память')),
                ('battery_capacity', models.CharField(max_length=250, verbose_name='Емкость аккамулятора')),
                ('sd', models.BooleanField(default=True)),
                ('main_camera', models.CharField(max_length=250, verbose_name='Главная камера')),
                ('frontal_camera', models.CharField(max_length=250, verbose_name='Фронтальная камера')),
                ('processor', models.CharField(max_length=250, verbose_name='Процессор')),
                ('color', models.CharField(max_length=250, verbose_name='Цвет')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('battery_capacity', models.CharField(max_length=250, verbose_name='Емкость аккамулятора')),
                ('connection', models.CharField(max_length=250, verbose_name='Подключение')),
                ('microphone', models.BooleanField(default=True)),
                ('weight', models.CharField(max_length=250, verbose_name='Вес')),
                ('manufacturer', models.CharField(max_length=250, verbose_name='Производитель')),
                ('color', models.CharField(max_length=250, verbose_name='Цвет')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
