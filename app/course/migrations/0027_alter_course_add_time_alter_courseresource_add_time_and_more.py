# Generated by Django 4.0.2 on 2022-05-06 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0026_alter_course_add_time_alter_courseresource_add_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 21, 6, 26, 654960), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 21, 6, 26, 657952), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 21, 6, 26, 655961), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 21, 6, 26, 658953), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 6, 21, 6, 26, 656957), verbose_name='添加时间'),
        ),
    ]
