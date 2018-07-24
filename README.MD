# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB04 Django 模板
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-template.html)  

准备工作:
开启命令行并进入工程所在路径

### 1. 新建项目(Project)和应用(App)
在命令行中输入:

django-admin startproject zqxt_tmpl
cd zqxt_tmpl
python manage.py startapp learn

zqxt_tmpl 为项目名称, learn为应用名称

### 2. 修改文件

修改 `zqxt_tmpl/zqxt_tmpl/settings.py`  将App添加到列表中  

修改 `zqxt_tmpl/learn/views.py` 添加视图函数 index()  

在 `learn`目录下新建一个 `templates` 文件夹，里面新建一个 `home.html`  

修改 `home.html` 文件的内容

修改 zqxt_views/zqxt_views/urls.py 添加新的URL

### 3. 创建数据库表

注意本节并未使用该功能, 此操作仅用于去除运行时的提示信息(提示要创建数据库等等)  

在命令行中输入:
> python manage.py migrate  

### 4. 运行项目

在命令行中输入:  

> python manage.py runserver 8002

在浏览器中访问:  

> http://127.0.0.1:8002  

模板中的一些循环，条件判断，标签，过滤器等使用请看下一节的内容。  
