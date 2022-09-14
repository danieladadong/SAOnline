# Generated by Django 4.0.2 on 2022-04-17 23:34

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0022_alter_course_add_time_alter_course_degree_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 23, 34, 41, 884338), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='course',
            name='detail',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='课程详情'),
        ),
        migrations.AlterField(
            model_name='courseresource',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 23, 34, 41, 886336), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 23, 34, 41, 885338), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='eights',
            field=models.CharField(db_column='eights', max_length=50, null=True, verbose_name='第八节'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='fives',
            field=models.CharField(db_column='fives', max_length=50, null=True, verbose_name='第五节'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='fours',
            field=models.CharField(db_column='fours', max_length=50, null=True, verbose_name='第四节'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='nines',
            field=models.CharField(db_column='nines', max_length=50, null=True, verbose_name='第九节'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='ones',
            field=models.CharField(db_column='ones', max_length=50, null=True, verbose_name='第一节'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sevens',
            field=models.CharField(db_column='sevens', max_length=50, null=True, verbose_name='第七节'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='sixs',
            field=models.CharField(db_column='sixs', max_length=50, null=True, verbose_name='第六节'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='threes',
            field=models.CharField(db_column='threes', max_length=50, null=True, verbose_name='第三节'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='twos',
            field=models.CharField(db_column='twos', max_length=50, null=True, verbose_name='第二节'),
        ),
        migrations.AlterField(
            model_name='usercourse',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 23, 34, 41, 887338), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='video',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 17, 23, 34, 41, 886336), verbose_name='添加时间'),
        ),
    ]
