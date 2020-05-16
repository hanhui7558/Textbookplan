from django.db import models
from django.contrib.auth.models import AbstractUser, User

'''
class MyUser(AbstractUser):
    # 需要绑定教学任务书的外键
    # 与User模型构成一对一的关系

    unit = models.CharField('单位', max_length=20, default='暂无信息')
    # useract = models.CharField('账号', max_length=20, default=0)
    # userpsd = models.CharField('密码', max_length=20, default=0)

    def __str__(self):
        return self.unit

    # class Meta:
    #     verbose_name = '用户信息'
    #     verbose_name_plural = '用户信息'
'''

class MyUser(models.Model):
    # 与 User 模型构成一对一的关系
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='myuser',default="")
    # 用户单位
    unit = models.CharField('单位', max_length=20, default='暂无信息')

    def __str__(self):
        return 'user {}'.format(self.user.username)