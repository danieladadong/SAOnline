# Generated by Django 4.0.2 on 2022-04-10 02:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0021_alter_course_add_time_alter_course_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 10, 42, 37, 133116), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='course',
            name='degree',
            field=models.CharField(max_length=10, verbose_name='难度'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 10, 42, 37, 136139), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 10, 42, 37, 134123), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 10, 42, 37, 136139), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 10, 10, 42, 37, 135120), verbose_name='添加时间'),
        ),
    ]