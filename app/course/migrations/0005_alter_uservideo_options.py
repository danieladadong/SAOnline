# Generated by Django 4.0.2 on 2022-02-13 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_uservideo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uservideo',
            options={'verbose_name': '用户学习视频', 'verbose_name_plural': '用户学习视频'},
        ),
    ]