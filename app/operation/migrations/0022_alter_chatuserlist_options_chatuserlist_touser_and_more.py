# Generated by Django 4.0.2 on 2022-05-05 23:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
        ('operation', '0021_alter_coursecomment_add_time_alter_notice_add_time_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatuserlist',
            options={'verbose_name': '聊天用户列表', 'verbose_name_plural': '聊天用户列表'},
        ),
        migrations.AddField(
            model_name='chatuserlist',
            name='touser',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='organization.teacher', verbose_name='聊天用户'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatuserlist',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='coursecomment',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 23, 5, 9, 81690), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 23, 5, 9, 85694), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfavorite',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 23, 5, 9, 82693), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usermessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 5, 23, 5, 9, 83692), verbose_name='添加时间'),
        ),
        migrations.AlterModelTable(
            name='chatuserlist',
            table='chatuserlist',
        ),
    ]