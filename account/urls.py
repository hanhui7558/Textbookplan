from django.urls import path
from .views import *

urlpatterns = [
    # 用户登录
    path('user.html', userLogin, name='userLogin'),
    path('login/', userLogin, name='userLogin'),
]
