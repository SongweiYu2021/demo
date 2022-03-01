from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("首页.<a href='/register'>注册</a>.<a href='/login'>登录</a>")
    return render(request, 'base.html')
#注册
def register(request):
    return HttpResponse("注册.<a href='/'>首页</a>")
#登录
def login(request):
    return HttpResponse("登录.<a href='/'>首页</a>")

def community(request):
    return HttpResponse("社区")
