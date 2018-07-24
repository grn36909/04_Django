# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB03 Django URL name详解
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-url-name.html)  

准备工作:
开启命令行并进入工程所在路径

### 1. 修改文件

修改 `zqxt_views/calc/views.py` 添加视图函数 index()  

修改 `zqxt_views/zqxt_views/settings.py`  将App添加到列表中  

修改 `zqxt_views/zqxt_views/urls.py` 添加新的URL

### 2. 建立html文件

在 'zqxt_views/calc/' 内新建 'templates' 文件夹  
在 'templates' 内新建 'home.html' 文件并修改文件

### 3. 通过 reverse() 来获取对应的网址(活链接)

修改 `zqxt_views/manage.py` 导入 reverse() 函数  

> from django.urls import reverse  

修改 `zqxt_views/calc/views.py` 添加URL转换函数 old_add2_redirect()  






### 1.3 运行项目

在命令行中输入:  

> python manage.py runserver 8002  

默认端口是 `8000`，上面使用了自定义端口 `8002`  
如果提示 `Error: That port is already in use.`   
我们可以在后面加上端口号`8001`，`8888`等  

在浏览器中访问:  
> http://127.0.0.1:8002/add/?a=4&b=5  


### 2.采用 `/add/3/4/` 这样的网址的方式

修改 `zqxt_views/calc/views.py` 添加视图函数 add2()  

修改 `zqxt_views/urls.py` 添加新的 url  

在浏览器中访问:
>  http://127.0.0.1:8002/add/4/5/  
