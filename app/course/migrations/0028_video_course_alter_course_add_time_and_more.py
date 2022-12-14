# Generated by Django 4.0.2 on 2022-05-17 10:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0027_alter_course_add_time_alter_courseresource_add_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course.course', verbose_name='所属课程'),
        ),
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 10, 32, 238511), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 10, 32, 241509), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 10, 32, 239510), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 10, 32, 243510), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 10, 32, 240511), verbose_name='添加时间'),
        ),
    ]
