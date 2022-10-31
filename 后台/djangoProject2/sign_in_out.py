from django.http import JsonResponse

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from moviesapp.models import Movie
import json

# 登录处理
def signin(request):
    return render(request,"signin.html")

def dosignin(request):
    # 从 HTTP POST 请求中获取用户名、密码参数
    userName = request.POST.get('username')
    passWord = request.POST.get('password')

    # 使用 Django auth 库里面的 方法校验用户名、密码
    user = authenticate(username=userName, password=passWord)

    # 如果能找到用户，并且密码正确
    if user is not None:
        if user.is_active:
            if user.is_superuser:
                login(request, user)
                # 在session中存入用户类型
                request.session['usertype'] = 'mgr'

                return render(request,"main.html")
            else:
                return render(request,"returnsignin.html")
        else:
            return render(request,"returnsignin.html")

    # 否则就是用户名、密码有误
    else:
        return render(request,"returnsignin.html")

# 登出处理
def do_signout(request):
    # 使用登出方法
    logout(request)
    return render(request,"signin.html")

