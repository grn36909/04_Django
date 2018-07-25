# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB05 Django 模板进阶(template2)
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-template2.html)  

Django模板中的循环，条件判断，常用的标签，过滤器的使用  

- 列表，字典，类的实例的使用
- 循环：迭代显示列表，字典等中的内容
- 条件判断：判断是否显示该内容，比如判断是手机访问，还是电脑访问，给出不一样的代码。
- 标签：for，if 这样的功能都是标签。
- 过滤器：管道符号后面的功能，比如{{ var|length }}，求变量长度的 length 就是一个过滤器。

准备工作:
使用 EB04 的项目和应用
开启命令行并进入工程所在路径

### 1. 显示一个基本的字符串在网页上

修改 `zqxt_tmpl/learn/views.py` 添加视图函数 home_text()

修改 `zqxt_tmpl/zqxt_tmpl/urls.py`  将视图对应到 url

修改 `home.html` 文件的内容

在命令行中输入:  

> python manage.py runserver 8002

在浏览器中访问:  

> http://127.0.0.1:8002  

### 2. 讲解了基本的 `for` 循环 和 `List` 内容的显示

修改 `zqxt_tmpl/learn/views.py` 添加视图函数 home_for()

修改 `zqxt_tmpl/zqxt_tmpl/urls.py`  将视图对应到 url

修改 `home.html` 文件的内容

在命令行中输入:  

> python manage.py runserver 8002

在浏览器中访问:  

> http://127.0.0.1:8002/for  

### 3. 显示字典中内容

修改 `zqxt_tmpl/learn/views.py` 添加视图函数 home_dict()

修改 `zqxt_tmpl/zqxt_tmpl/urls.py`  将视图对应到 url

修改 `home.html` 文件的内容

在命令行中输入:  

> python manage.py runserver 8002

在浏览器中访问:  

> http://127.0.0.1:8002/dict 

### 4. 在模板进行 条件判断和 for 循环的详细操作

修改 `zqxt_tmpl/learn/views.py` 添加视图函数 home_list()

修改 `zqxt_tmpl/zqxt_tmpl/urls.py`  将视图对应到 url

修改 `home.html` 文件的内容

在命令行中输入:  

> python manage.py runserver 8002

在浏览器中访问:  

> http://127.0.0.1:8002/list

for 循环可用的相关变量

| 变量 | 描述 |
| ---- | ---- |
| forloop.counter | 索引从 1 开始算 |
| forloop.counter0 | 索引从 0 开始算 |
| forloop.revcounter | 索引从最大长度到 1 |
| forloop.revcounter0 | 索引从最大长度到 0 |
| forloop.first | 当遍历的元素为第一项时为真 |
| forloop.last | 当遍历的元素为最后一项时为真 |
| forloop.parentloop | 用在嵌套的 for 循环中，获取上一层 for 循环的 forloop |

- 获取当前用户  {{ request.user }}  
- 获取当前网址  {{ request.path }}  
- 获取当前 GET 参数  {{ request.GET.urlencode }}  
