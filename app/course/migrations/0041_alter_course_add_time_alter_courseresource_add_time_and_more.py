# Generated by Django 4.0.2 on 2022-05-19 13:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0040_alter_course_add_time_alter_courseresource_add_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 13, 45, 36, 335031), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 13, 45, 36, 337027), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 13, 45, 36, 336027), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 13, 45, 36, 337027), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 19, 13, 45, 36, 336027), verbose_name='添加时间'),
        ),
    ]
