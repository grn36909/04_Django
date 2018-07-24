from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect

def index(request):                     # home.html
    return render(request, 'home.html')

def add(request):                       # 采用 /add/?a=4&b=5 这样GET方法进行
    # a = request.GET['a']              # 当没有传递'a'时会报错
    # b = request.GET['b']
    a = request.GET.get('a', 0)         # 当没有传递'a'的时候返回'0'
    b = request.GET.get('b', 0)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):                # 采用 /add/3/4/ 这样的网址的方式
    c = int(a) + int(b)
    return HttpResponse(str(c))

def old_add2_redirect(request, a, b):   # 使用reverse()函数转换url, 转换后可在其它函数中使用
    return HttpResponseRedirect(        # http请求重定向
        reverse('add2', args=(a, b))    # 将url转换为add2的格式
    )