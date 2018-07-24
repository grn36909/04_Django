from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def add(request):                   # 采用 /add/?a=4&b=5 这样GET方法进行
    # a = request.GET['a']          # 当没有传递'a'时会报错
    # b = request.GET['b']
    a = request.GET.get('a', 0)     # 当没有传递'a'的时候返回'0'
    b = request.GET.get('b', 0)
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):            # 采用 /add/3/4/ 这样的网址的方式
    c = int(a) + int(b)
    return HttpResponse(str(c))
