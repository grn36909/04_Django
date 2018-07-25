# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB06 Django 模型（数据库）
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-models.html)  

Django 模型是与数据库相关的，  
与数据库相关的代码一般写在 `models.py` 中，  
Django 支持 `sqlite3`, `MySQL`, `PostgreSQL`等数据库，  
只需要在 `settings.py` 中配置即可，  
不用更改 `models.py` 中的代码，丰富的API极大的方便了使用。  

准备工作:  
开启命令行并进入工程所在路径  

### 1. 新建项目(Project)和应用(App)

在命令行中输入:

> django-admin.py startproject learn_models     # 新建一个项目'learn_models'  
> cd learn_models                               # 进入到该项目的文件夹  
> django-admin.py startapp people               # 新建一个应用'people'  

### 2. 修改文件

修改 `learn_models/learn_models/settings.py` 将App添加到列表中  

修改 `learn_models/people/models.py` 添加`Person`类  

### 3. 创建数据表

进入 `manage.py` 文件所在路径, 并在命令行输入:  

> python manage.py makemigrations  
> python manage.py migrate  

### 4. 使用 Django 提供的 QuerySet API

进入 `manage.py` 文件所在路径, 并在命令行输入:  

> python manage.py shell  

在 shell 中输入下面的代码：  

> from people.models import Person  
> Person.objects.create(name="grn31", age=24)  

返回结果：  

> <Person: grn31>  

在 shell 中输入下面的代码：  

> Person.objects.get(name="grn31")  

返回结果：  

> <Person: grn31>  

----

**新建一个对象的方法有以下几种**：

1.  > Person.objects.create(name=name,age=age)  

2.  > p = Person(name="WZ", age=23)`  
    > p.save()  

3.  > p = Person(name="TWZ")  
    > p.age = 23
    > p.save()

4.  > Person.objects.get_or_create(name="WZT", age=23)

    这种方法是防止重复很好的方法，但是速度要相对慢些。  
    返回一个元组，第一个为`Person`对象，第二个为`True`或`False`, 新建时返回的是`True`, 已经存在时返回`False`.  

**获取对象有以下方法：**

1.    > Person.objects.all()  

2.    > Person.objects.all()[:10]  

    切片操作，获取10个人，不支持负索引，切片可以节约内存  

3.    > Person.objects.get(name=name)  

    get是用来获取一个对象的，如果需要获取满足条件的一些人，就要用到filter  

4.    > Person.objects.filter(name="abc")  # 等于Person.objects.filter(name__exact="abc") 名称严格等于 "abc" 的人  

5.    > Person.objects.filter(name__iexact="abc")  # 名称为 abc 但是不区分大小写，可以找到 ABC, Abc, aBC，这些都符合条件  

6.    > Person.objects.filter(name__contains="abc")  # 名称中包含 "abc"的人  

7.    > Person.objects.filter(name__icontains="abc")  #名称中包含 "abc"，且abc不区分大小写  

8.    > Person.objects.filter(name__regex="^abc")  # 正则表达式查询  

9.    > Person.objects.filter(name__iregex="^abc")  # 正则表达式, 不区分大小写  

    filter是找出满足条件的，当然也有排除符合某条件的  

10.  > Person.objects.exclude(name__contains="WZ")  # 排除包含 WZ 的Person对象  

11.  > Person.objects.filter(name__contains="abc").exclude(age=23)  # 找出名称含有abc, 但是排除年龄是23岁的  
