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

在 `zqxt_views/calc/` 内新建 `templates` 文件夹  
在 `templates` 内新建 `home.html` 文件并修改文件  

### 3. 通过 reverse() 来获取对应的网址(重定向)

修改 `zqxt_views/manage.py` 导入 `reverse()` 函数  

> from django.urls import reverse  

修改 `zqxt_views/calc/views.py` 添加URL转换函数 `old_add2_redirect()`  

修改 `zqxt_views/zqxt_views/urls.py` 添加新的URL  

### 4. 运行项目

在命令行中输入:  

> python manage.py runserver 8002  

在浏览器中访问:  

> http://127.0.0.1:8002  
