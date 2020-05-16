from django.db import models


# Create your models here.
from account.models import MyUser


class TeachingTask (models.Model):
    id = models.AutoField(primary_key=True)
    courseunit = models.CharField('开课单位', max_length=50)
    courseid = models.IntegerField('课程编号', default=0)
    coursename = models.CharField('课程名称', max_length=50)
    xueshi = models.IntegerField('总学时', default=0)
    teaching = models.IntegerField('理论', default=0)
    practice = models.IntegerField('实践', default=0)
    xuefen = models.FloatField('学分', default=0)
    grade = models.IntegerField('年级', default=0)
    major = models.CharField('专业', max_length=50)
    studentnum = models.IntegerField('人数', default=0)
    xiaoqu = models.CharField('校区', max_length=50)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name=u'单位')

    # 设置返回值
    def __str__(self):
        return self.courseunit

    class Meta:
        verbose_name = '教学计划'
        verbose_name_plural = '教学计划'
