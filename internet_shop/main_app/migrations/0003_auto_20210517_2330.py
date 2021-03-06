# Generated by Django 3.2 on 2021-05-17 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_audio_smartphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='for_anonymous_user',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='in_order',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='audio',
            name='battery_capacity',
            field=models.CharField(max_length=250, verbose_name='Емкость аккумулятора'),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='battery_capacity',
            field=models.CharField(max_length=250, verbose_name='Емкость аккумулятора'),
        ),
    ]
