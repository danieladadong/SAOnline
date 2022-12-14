# Generated by Django 4.0.2 on 2022-04-05 02:45

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_table'),
        ('course', '0017_alter_course_add_time_alter_courseresource_add_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 5, 10, 45, 33, 482777), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 5, 10, 45, 33, 485784), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 5, 10, 45, 33, 483776), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 5, 10, 45, 33, 486782), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 5, 10, 45, 33, 483776), verbose_name='添加时间'),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(db_column='label', max_length=50, verbose_name='周几')),
                ('ones', models.CharField(db_column='ones', max_length=50, verbose_name='第一节')),
                ('twos', models.CharField(db_column='twos', max_length=50, verbose_name='第二节')),
                ('threes', models.CharField(db_column='threes', max_length=50, verbose_name='第三节')),
                ('fours', models.CharField(db_column='fours', max_length=50, verbose_name='第四节')),
                ('fives', models.CharField(db_column='fives', max_length=50, verbose_name='第五节')),
                ('sixs', models.CharField(db_column='sixs', max_length=50, verbose_name='第六节')),
                ('sevens', models.CharField(db_column='sevens', max_length=50, verbose_name='第七节')),
                ('eights', models.CharField(db_column='eights', max_length=50, verbose_name='第八节')),
                ('nines', models.CharField(db_column='nines', max_length=50, verbose_name='第九节')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofile', verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户课表',
                'verbose_name_plural': '用户课表',
                'db_table': 'schedule',
            },
        ),
    ]
