# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB02 Django 视图与网址进阶
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-views-urls2.html)  

准备工作:
开启命令行并进入工程所在路径

### 1. 采用 `/add/?a=4&b=5` 这样GET方法进行

#### 1.1 新建项目(Project)和应用(App)

在命令行中输入:  

> django-admin startproject zqxt_views
> cd zqxt_views
> python manage.py startapp calc 

`mysite`为项目名称

### 1.2 修改文件

修改 `zqxt_views/calc/views.py` 添加视图函数 add()  

修改 `zqxt_views/zqxt_views/urls.py`  添加一个网址来对应我们刚才新建的视图函数  

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
