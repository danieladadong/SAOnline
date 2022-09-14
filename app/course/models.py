from django.db import models
import datetime
from app.organization.models import Organization, Teacher
from app.users.models import UserProfile
from ckeditor.fields import RichTextField


# Create your models here.
class Course(models.Model):
    organization = models.ForeignKey(Organization, verbose_name="所属机构", on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, verbose_name="授课教师", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="名称", max_length=50)
    desc = models.CharField(verbose_name="课程描述", max_length=255)
    detail = RichTextField(null=True, blank=True, verbose_name="课程详情")
    image = models.ImageField(verbose_name="封面图", upload_to='course/%Y/%m', null=True)
    degree = models.CharField(verbose_name="难度", max_length=10)
    is_publish = models.BooleanField(verbose_name="是否发布", default=False)
    learn_times = models.FloatField(verbose_name="课程时长(分钟数)", default=0)
    click_nums = models.IntegerField(verbose_name="点击数", default=0)
    learn_nums = models.IntegerField(verbose_name="学习人数", default=0)
    fav_nums = models.IntegerField(verbose_name="收藏数", default=0)
    category = models.CharField(verbose_name="分类", max_length=20)
    tag = models.CharField(verbose_name="标签", max_length=20)
    you_need_know = models.CharField(verbose_name="课程须知", max_length=255, default="本课程需要静心阅读")
    teacher_tell = models.CharField(verbose_name="老师告诉你", max_length=255, default="好好学习，天天向上")
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        db_table = "course"
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="所属课程", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="章节名", max_length=20)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        db_table = "lesson"
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="所属章节", on_delete=models.CASCADE, related_name="videos")
    course = models.ForeignKey(Course, verbose_name="所属章节", on_delete=models.CASCADE, default=None)
    name = models.CharField(verbose_name="视频名", max_length=20)
    url = models.FileField(verbose_name="视频文件", upload_to="video/%Y%m")
    learn_times = models.FloatField(verbose_name="视频时长(分钟数)", default=0)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        db_table = "video"
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="所属课程", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="资源名", max_length=20)
    resource = models.FileField(verbose_name="资源文件", upload_to='course/resource/%Y%m')
    isVideo = models.BooleanField(verbose_name="是否为视频", db_column="isvideo", default=False)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        db_table = "courseresource"
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserCourse(models.Model):
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.datetime.now())

    class Meta:
        db_table = "usercourse"
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserVideo(models.Model):
    video = models.ForeignKey(Video, verbose_name="视频", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name="章节", on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)
    learned_time = models.FloatField(verbose_name="观看位置")
    is_finish = models.BooleanField(verbose_name="是否看完", default=False)

    class Meta:
        db_table = "uservideo"
        verbose_name = "用户学习视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Schedule(models.Model):
    label = models.CharField(verbose_name="周几", db_column="label", max_length=50)
    ones = models.CharField(verbose_name="第一节", db_column="ones", max_length=50, null=True, default="空")
    twos = models.CharField(verbose_name="第二节", db_column="twos", max_length=50, null=True, default="空")
    threes = models.CharField(verbose_name="第三节", db_column="threes", max_length=50, null=True, default="空")
    fours = models.CharField(verbose_name="第四节", db_column="fours", max_length=50, null=True, default="空")
    fives = models.CharField(verbose_name="第五节", db_column="fives", max_length=50, null=True, default="空")
    sixs = models.CharField(verbose_name="第六节", db_column="sixs", max_length=50, null=True, default="空")
    sevens = models.CharField(verbose_name="第七节", db_column="sevens", max_length=50, null=True, default="空")
    eights = models.CharField(verbose_name="第八节", db_column="eights", max_length=50, null=True, default="空")
    nines = models.CharField(verbose_name="第九节", db_column="nines", max_length=50, null=True, default="空")
    user = models.ForeignKey(UserProfile, verbose_name="用户", on_delete=models.CASCADE)

    class Meta:
        db_table = "schedule"
        verbose_name = "用户课表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
