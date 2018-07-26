from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from tools.forms import AddForm

def index(request):
    if request.method == 'POST':        # 当提交表单时
     
        form = AddForm(request.POST)    # form 包含提交的数据
         
        if form.is_valid():             # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
     
    else:                               # 当正常访问时
        form = AddForm()                # 显示 form
    return render(request, 'index.html', {'form': form})
