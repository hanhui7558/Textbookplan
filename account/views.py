from django.shortcuts import render, redirect
from django.urls import reverse
from account.models import MyUser
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from index.models import TeachingTask

#
# def account(request):
# return render(request, 'account.html', locals())
def userLogin(request):
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password', '')
        user = authenticate(username=u, password=p)

        if user:
            if user.is_active:
                login(request, user)
                kwargs = {'id': request.user.id, 'page': 1}
                # 增加转向以后的路由
                return redirect(reverse('index', kwargs=kwargs))
            else:
                tips = '账号密码错误，请联系管理员'
        else:
            tips = '用户不存在，请联系管理员'
    else:
        if request.user.username:
            kwargs = {'id': request.user.id, 'page': 1}
            return redirect(reverse('index', kwargs=kwargs))
            # return redirect(reverse('index', kwargs=kwargs))
        return render(request, 'user.html')

    return render(request, 'user.html', locals())
