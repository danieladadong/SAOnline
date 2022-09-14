from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
import datetime
# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女'),
    )
    nick_name = models.CharField(verbose_name="昵称", default='', max_length=20)
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(verbose_name="性别", choices=GENDER_CHOICES, max_length=6, default='male')
    address = models.CharField(verbose_name="地址", max_length=100, default='')
    mobile = models.CharField(verbose_name="手机号", max_length=11, default='')
    image = models.ImageField(verbose_name="头像", upload_to='image/%Y/%m', default='image/2022/05/TX8620_12.jpg')

    class Meta:
        db_table = "userprofile"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.nick_name