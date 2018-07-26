# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB11 后台
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-admin.html)  

django的后台我们只要加少些代码，就可以实现强大的功能。  

与后台相关文件：每个app中的 `admin.py` 文件与后台相关。  

`准备工作:`
开启命令行并进入工程所在路径

### 1. 新建项目(Project)和应用(App)

在命令行中输入:  

```dos
django-admin startproject zqxt_admin
cd learn_models
django-admin startapp blog
```
项目：`zqxt_admin`   
应用：`blog`   

### 2. 修改文件

修改 `zqxt_admin/blog/models.py` 添加 `Article` 类  

修改 `zqxt_admin/zqxt_admin/settings.py` 将应用添加到 `INSTALLED_APPS` 元组  

### 3. 同步所有的数据表

进入 `manage.py` 文件所在路径, 并在命令行输入:  

```dos
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
创建管理员时，使用名称： `admin`， 密码：`admin1234`  

- **makemigrations**  
在该 app下建立 `migrations` 目录，并记录下你所有的关于 `modes.py` 的改动，比如 `0001_initial.py`， 但是这个改动还没有作用到数据库文件  

- **migrate**  
将该改动作用到数据库文件，比如产生 table 之类  

- **createsuperuser**  
创建管理员  

#### 4. 注册站点

修改 `zqxt_admin/blog/admin.py` 注册站点 `Article` 类

#### 5. 运行开发服务器

进入 `manage.py` 文件所在路径, 并在命令行输入:  

```dos
python manage.py runserver 8003
```

打开浏览器并访问:  

> http://localhost:8003/admin/  

输入设定的帐号和密码  
> admin ---- admin1234  

#### 6. 修正文章标题显示

修改 `zqxt_admin/blog/models.py` 并在 `Article` 类的末尾加入:  

```python
def __str__(self):
        return self.title
```

#### 7. 在列表显示与字段相关的其它内容

1. 在文章列表中显示其它信息: `标题`, `发布时间`, `更新时间`  

修改 `zqxt_admin/blog/admin.py`  加入 `ArticleAdmin` 类,并修改 `admin.site.register()` 参数

2. 添加非字段内容，或者字段相关的内容 `Person`  

修改 `zqxt_admin/blog/models.py`  添加 `Person` 类  

修改 `zqxt_admin/blog/admin.py`  加入 `Person` 引用, `PersonAdmin` 类和 `admin.site.registe()` 调用  

3. 因新添加了 `Person` 内容, 所以需要重新同步数据表

进入 `manage.py` 文件所在路径, 并在命令行输入:  

```dos
python manage.py makemigrations
python manage.py migrate
```
