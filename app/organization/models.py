from django.db import models
import datetime


# Create your models here.
class City(models.Model):
    name = models.CharField(verbose_name="城市", max_length=20)

    class Meta:
        db_table = "city"
        verbose_name = "城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Organization(models.Model):
    ORG_CHOICES = (
        ('pxjg', '培训机构'),
        ('gx', '高校'),
        ('gr', '个人'),
    )

    name = models.CharField(verbose_name="机构名称", max_length=20)
    desc = models.TextField(verbose_name="机构描述")
    category = models.CharField(verbose_name="机构类别", max_length=20, choices=ORG_CHOICES, default='pxjg')
    tag = models.CharField(verbose_name="机构标签", max_length=20, default="全国知名")
    image = models.ImageField(verbose_name="封面图", upload_to='organization/%Y/%m')
    address = models.CharField(verbose_name="机构地址", max_length=200)
    city = models.ForeignKey(City, verbose_name="所在城市", on_delete=models.CASCADE)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    learn_nums = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    course_nums = models.IntegerField(verbose_name="课程数", default=0)
    is_authentication = models.BooleanField(verbose_name="是否认证", default=False)
    is_gold = models.BooleanField(verbose_name="金牌机构", default=False)

    class Meta:
        db_table = "organization"
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(models.Model):
    organization = models.ForeignKey(Organization, verbose_name="所属机构", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="姓名", max_length=20)
    age = models.IntegerField(verbose_name="年龄", default=0)
    image = models.ImageField(verbose_name="头像", upload_to='teacher/%Y/%m', default='', null=True, blank=True)
    work_year = models.IntegerField(verbose_name="工作年限", default=0)
    work_company = models.CharField(verbose_name="就职公司", max_length=50)
    work_position = models.CharField(verbose_name="工作岗位", max_length=50)
    points = models.CharField(verbose_name="教学特点", max_length=50)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)

    class Meta:
        db_table = "teacher"
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
