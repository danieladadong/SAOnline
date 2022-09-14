# Generated by Django 4.0.2 on 2022-05-17 10:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0030_alter_course_add_time_alter_courseresource_add_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='course',
        ),
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 12, 33, 200175), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 12, 33, 203172), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 12, 33, 202173), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 12, 33, 204175), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 12, 33, 202173), verbose_name='添加时间'),
        ),
    ]
