from django.db import models
from app.course.models import Course
from app.users.models import UserProfile
# Create your models here.
# 题库表
class QuestionBank(models.Model):
    id = models.AutoField('序号',primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='科目')
    title = models.TextField('题目')
    qtype = models.CharField('题目类型',choices=(('单选','单选'),),max_length=40)
    a = models.CharField('A选项',max_length=40)
    b = models.CharField('B选项',max_length=40)
    c = models.CharField('C选项',max_length=40)
    d = models.CharField('D选项',max_length=40)
    answer = models.CharField('答案',choices=(('A','A'),('B','B'),('C','C'),('D','D')),max_length=4)
    difficulty = models.CharField('难度',choices=(('easy','简单'),('middle','中等'),('difficult','难')),max_length=10)
    score = models.IntegerField('分值')

    class Meta:
        db_table = "questionbank"
        verbose_name = '题库'
        # 显示的表名
        verbose_name_plural = '题库'
    def __str__(self):
        return self.title

# 试卷表
class ExamPaper(models.Model):
    id = models.AutoField('序号',primary_key=True)
    title = models.CharField('题目',max_length=40,unique=True)
    pid = models.ManyToManyField(QuestionBank)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='科目')
    time = models.IntegerField('考试时长',help_text='单位是分钟')
    examtime = models.DateTimeField('上次考试时间')

    class Meta:
        db_table = "exampaper"
        verbose_name = '试卷'
        verbose_name_plural = '试卷'
    def __str__(self):
        return self.title


# # 学生成绩表
class Record(models.Model):
    id = models.AutoField('序号',primary_key=True)
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,verbose_name='学号')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='考试科目')
    exampaper = models.ForeignKey(ExamPaper,on_delete=models.CASCADE,verbose_name='试卷')
    grade = models.FloatField('成绩')
    rtime = models.DateTimeField('考试时间',blank=True,null=True)

    class Meta:
        db_table = "record"
        verbose_name = '学生成绩'
        verbose_name_plural = '学生成绩'

