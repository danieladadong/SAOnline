# Generated by Django 4.0.2 on 2022-05-17 10:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0028_alter_coursecomment_add_time_alter_notice_add_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 27, 0, 16886), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 27, 0, 19893), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 27, 0, 17892), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 10, 27, 0, 18896), verbose_name='添加时间'),
        ),
    ]