# Generated by Django 4.0.2 on 2022-02-19 01:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_delete_usercourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursecomment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 9, 56, 51, 273393), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 9, 56, 51, 274391), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 19, 9, 56, 51, 274391), verbose_name='添加时间'),
        ),
    ]
