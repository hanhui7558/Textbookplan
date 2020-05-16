from django.db import models
from account.models import MyUser
from index.models import TeachingTask


class BookOrd (models.Model):
    id = models.AutoField(primary_key=True)
    stulevel = models.CharField(max_length=20, default=0)
    coursetitle = models.CharField(max_length=20, default=0)
    # 开课学生字段：年级、专业、班级
    tbname = models.CharField(max_length=20, default=0)
    tbversion = models.CharField(max_length=20, default=0)
    tbpublish = models.CharField(max_length=20, default=0)
    tbauthor = models.CharField(max_length=20, default=0)
    tbisbn = models.CharField(max_length=20, default=0)
    tbpurpose = models.CharField(max_length=20, default=0)
    # 联系人字段：联系人、手机
    tbfteach = models.CharField(max_length=10, default=True)
    # teachingtask = models.ForeignKey (TeachingTask, on_delete=models.CASCADE)
    teachingtask = models.OneToOneField(TeachingTask, on_delete=models.CASCADE, verbose_name='教学计划')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, verbose_name='用户')


# 设置返回值
def __str__(self):
    return self.id
    # return self.coursetitle


class Meta:
    verbose_name = '教材征订'
    verbose_name_plural = '教材征订'
