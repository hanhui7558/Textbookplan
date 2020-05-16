from django.urls import path
from django.views.generic import RedirectView
from .views import *

urlpatterns = [
    # path('', index, name='index'),
    # 首页地址自动跳转用户登录页面
    path('', RedirectView.as_view(url='account/user.html')),
    # 教学任务列表
    path('<int:id>/<int:page>.html', index, name='index'),
]
# path('<int:id>/<int:page>.html',,)
# path('<int:id>/<int:page>.html', article, name='article'),
