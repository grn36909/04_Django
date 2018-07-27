# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB14 静态文件 (static-files)
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-static-files.html)  

静态文件是指 网站中的 js, css, 图片，视频等文件  

**准备工作**:  开启命令行并进入工程所在路径

### 1. 新建项目(Project)和应用(App)
在命令行中输入:

```dos
django-admin startproject zqxt_static
cd learn_models
django-admin startapp blog
```
项目：zqxt_static  
应用：blog  

### 2. 修改文件

修改文件 `zqxt_static/zqxt_static/settings.py` 将应用 blog 加入 `static` 相关代码  

修改文件 `zqxt_static/zqxt_static/settings.py` 添加 `static` 相关代码  

```python
# 当运行 python manage.py collectstatic 的时候
# STATIC_ROOT 文件夹 是用来将所有STATICFILES_DIRS中所有文件夹中的文件，以及各app中static中的文件都复制过来
# 把这些文件放到一起是为了用apache等部署的时候更方便
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')
 
# 其它 存放静态文件的文件夹，可以用来存放项目中公用的静态文件，里面不能包含 STATIC_ROOT
# 如果不想用 STATICFILES_DIRS 可以不用，都放在 app 里的 static 中也可以
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),
    '/path/to/others/static/',  # 用不到的时候可以不写这一行
)
 
# 这个是默认设置，Django 默认会在 STATICFILES_DIRS中的文件夹 和 各app下的static文件夹中找文件
# 注意有先后顺序，找到了就不再继续找了
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)
```

静态文件放在对应的 app 下的 static 文件夹中 或者 STATICFILES_DIRS 中的文件夹中。  

将图像文件 `zqxt.png` 放入 `zqxt_static/blog/static/` 路径下  

也可以在 settings.py 中指定所有 app 共用的静态文件，比如 jquery.js 等  

将JS文件 `jquery.js` 放入 `zqxt_static/common_static/js/` 路径下  

### 3. 运行开发服务器

进入 `manage.py `文件所在路径, 并在命令行输入:  

```dos
python manage.py runserver 8004
```
打开浏览器并访问:  
> http://localhost:8004/static/zqxt.png  
> http://localhost:8004/static/js/jquery.js  
