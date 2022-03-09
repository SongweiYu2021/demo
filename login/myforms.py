from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="用户名username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label="验证码")

class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
        ('unknown', "未知")
    )

    username = forms.CharField(label="用户名username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码passord", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码confirm", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label="性别gender", choices=gender)
    captcha = CaptchaField(label='验证码captcha')
