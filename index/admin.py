from django.contrib import admin

# Register your models here.
from index.models import TeachingTask

# 注册TeachingTask
admin.site.register(TeachingTask)