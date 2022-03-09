from django.http import HttpResponse

def index(request):
    return HttpResponse("欢迎来到社区.<a href=''>首页</a>")


