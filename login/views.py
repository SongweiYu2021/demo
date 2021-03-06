from django.shortcuts import render, redirect
from . import models
from .myforms import UserForm
from .myforms import RegisterForm
import hashlib
from ns_community.models import Post

def index(request):
    pass
    return render(request, 'login/index.html')

def login(request):
    # session 不允许重复登录
    if request.session.get('is_login', None):
        return redirect('/index/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # 符合法性验证 密码长度 其他。。。
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对

                    # 往session字典内写入用户状态和数据：
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户名不存在"
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def profile(request):
    if not request.session.get('is_login', None):

        return redirect('/login/')

    return render(request, 'page.html')

def register(request):

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        #message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                    # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())

#密码，哈希加密
def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def logout(request):
    if not request.session.get('is_login', None):
        # 本来就没登录 不需要logout
        return redirect('/index/')
    request.session.flush()
    return redirect('/index/')

def community(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'community.html', context)

def about(request):
    pass
    return render(request, 'about.html')

def category(request):
    pass
    return render(request, 'category.html')
