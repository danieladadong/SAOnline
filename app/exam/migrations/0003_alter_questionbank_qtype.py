# Generated by Django 4.0.2 on 2022-05-18 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_record_exampaper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionbank',
            name='qtype',
            field=models.CharField(choices=[('单选', '单选')], max_length=40, verbose_name='题目类型'),
        ),
    ]
