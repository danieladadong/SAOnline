# Generated by Django 4.0.2 on 2022-03-20 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_course_add_time_alter_courseresource_add_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 20, 21, 11, 50, 246188), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 20, 21, 11, 50, 248188), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 20, 21, 11, 50, 247188), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 20, 21, 11, 50, 249187), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 20, 21, 11, 50, 248188), verbose_name='添加时间'),
        ),
    ]