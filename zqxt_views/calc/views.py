from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def add(request):
    # a = request.GET['a']          # 当没有传递时会报错
    # b = request.GET['b']
    a = request.GET.get('a', 0)     # 当没有传递’a‘的时候返回’0‘
    b = request.GET.get('b', 0)
    c = int(a)+int(b)
    return HttpResponse(str(c))
