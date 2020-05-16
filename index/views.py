from django.shortcuts import render, redirect
from index.models import TeachingTask
from account.models import MyUser
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
from django.urls import reverse

# from .form import MessageModelForm

# Create your views here.
def index(request, id, page):
    user = MyUser.objects.filter(id=id).first()
    if not user:
        return redirect(reverse('userLogin'))
    teachingtasks = TeachingTask.objects.filter(user_id=id).order_by('-id')
    paginator = Paginator(teachingtasks, 15)
    try:
        pageInfo = paginator.page(page)
    except PageNotAnInteger:
        # 如果参数page的数据类型不是整型，就返回第一页数据
        pageInfo = paginator.page(1)
    except EmptyPage:
        # 若用户访问的页面大于实际页数，则返回最后一页的数据
        pageInfo = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())



    # teachingtasks = TeachingTask.objects.all().order_by('-id')
    # return render(request, 'index.html', locals())
# 根据单位不同，显示不同的教学计划信息
# teachingtasks = TeachingTask.objects.filter(user_courseunit=courseunit).order_by('-id')
# 每页显示的信息条数
# paginator = Paginator.page(page)

# 分页部分
# paginator = Paginator(index, 3)
# # 获取url中的页码
# page = request.GET.get('page')
# # 将导航对象相应的页码内容返回给
# booklist = paginator.get_page(page)
# # 需要传递给模板（templates)的对象
# context = {'index': booklist}
