# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB12 表单
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-forms.html)  

有时候我们需要在前台用 `get` 或 `post` 方法提交一些数据，所以自己写一个网页，用到 `html 表单`的知识。  

`准备工作:`
开启命令行并进入工程所在路径

### 1. 新建项目(Project)和应用(App)

在命令行中输入:  

```dos
django-admin startproject zqxt_form2
cd learn_models
django-admin startapp tools
```
项目：`zqxt_form2`   
应用：`tools`   

### 2. 修改文件

新建文件 `zqxt_form2/tools/forms.py` 并添加 `AddForm` 类  

修改文件 `zqxt_form2/tools/views.py` 添加到 `index()` 函数  

新建文件 `zqxt_form2/tools/templates/index.html` 并添加内容  

修改文件 `zqxt_form2/zqxt_form2/urls.py`  将 `index()` 函数对应到 URL  

#### 3. 运行开发服务器

进入 `manage.py` 文件所在路径, 并在命令行输入:  

```dos
python manage.py runserver 8004
```

打开浏览器并访问:  

> http://localhost:8004  

在表单中输入数值后, 点击`提交`显示计算结果  
