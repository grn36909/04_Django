## Django 基础学习 

参考资源: by ziqiangxuetang.com

## 文件结构
---  

mysite  
├── manage.py  
└── mysite  
│   ├── __init__.py     # python包的目录结构必须的，与调用有关  
│   ├── settings.py     # Django 的设置，配置文件，比如 DEBUG 的开关，静态文件的位置等。  
│   ├── urls.py         # 网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数。  
│   └── wsgi.py         # 部署服务器时用到的 wsgi.py 文件  
└── learn/  
    ├── __init__.py  
    ├── admin.py        # 后台，可以用很少量的代码就拥有一个强大的后台  
    ├── models.py       # 与数据库操作相关，存入或读取数据时用到这个，当然用不到数据库的时候 你可以不使用。  
    ├── tests.py  
    └── views.py        # 处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。  


## EB01 Django 视图与网址
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-views-urls.html)  

准备工作:
开启命令行并进入工程所在路径

### 1. 新建项目(Project)

在命令行中输入:  

> django-admin startproject mysite  

'mysite'为项目名称

### 2. 新建应用(App)

在命令行中输入:  

> python manage.py startapp learn    

'learn'为应用名称

#### 2.1 添加App到应用列表中

修改 'mysite/mysite/settings.py' 将新定义的app加到settings.py中的INSTALL_APPS中  

#### 2.2 定义视图函数

修改 'mysite/learn/views.py' 添加 index() 函数

#### 2.3 定义视图函数相关的URL

修改 'mysite/mysite/urls.py' 将网址与函数关联

#### 2.4 运行项目

在命令行中输入:  

> python manage.py runserver  

打开浏览器,访问 http://127.0.0.1:8000/  

希望监听所有ip的8000端口时,应在命令行输入:

> python manage.py runserver 0.0.0.0:8000

在其它计算机上的浏览器输入本机ip浏览 http://x.x.x.x:8000/ 
