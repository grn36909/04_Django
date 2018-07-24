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

