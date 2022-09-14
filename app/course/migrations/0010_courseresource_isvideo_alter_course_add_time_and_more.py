# Generated by Django 4.0.2 on 2022-04-02 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_course_add_time_alter_courseresource_add_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseresource',
            name='isVideo',
            field=models.IntegerField(db_column='isvideo', default=0, verbose_name='是否为视频'),
        ),
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 18, 44, 33, 513503), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 18, 44, 33, 516504), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 18, 44, 33, 514503), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 18, 44, 33, 517503), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 2, 18, 44, 33, 515503), verbose_name='添加时间'),
        ),
    ]
