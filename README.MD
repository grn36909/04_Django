# Django 基础学习 

参考资源: by ziqiangxuetang.com

## EB13 配置 (settings)
----

[Learn-URL](https://code.ziqiangxuetang.com/django/django-settings.html)  

```python
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```

变量 `__file__` 可以获取到当前文件（包含这个代码的文件）的路径  
`os.path.dirname(__file__)`                  # 得到文件所在目录  
`os.path.dirname(os.path.dirname(__file__))` # 得到目录的上一级  
`os.path.dirname(BASE_DIR)`                  # 即为 项目 所在目录  

---

```python
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
```

`DEBUG＝True` 时，如果出现 bug 便于我们看见问题所在，但是部署时最好不要让用户看见bug的详情，可能一些不怀好心的人攻击网站，造成不必要的麻烦。  

---

```python
ALLOWED_HOSTS = ['*.besttome.com','www.ziqiangxuetang.com']
```
`ALLOWED_HOSTS` 允许你设置哪些域名可以访问，即使在 `Apache` 或 `Nginx` 等中绑定了，这里不允许的话，也是不能访问的。  
当 `DEBUG=False` 时，这个为必填项，如果不想输入，可以用 `ALLOW_HOSTS = ['*']` 来允许所有的。  

---

```python
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR,'static')
```
`static` 是静态文件所有目录，比如` jquery.js`, `bootstrap.min.css` 等文件。  

一般来说我们只要把静态文件放在 APP 中的 `static` 目录下，部署时用 `python manage.py collectstatic` 就可以把静态文件收集到（复制到） `STATIC_ROOT` 目录，但是有时我们有一些共用的静态文件，这时候可以设置 `STATICFILES_DIRS` 另外弄一个文件夹，如下：

```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),
    '/var/www/static/',
)
```
这样我们就可以把静态文件放在 `common_static` 和 `/var/www/static/` 中了，Django也能找到它们。

---

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
```
media文件夹用来存放用户上传的文件，与权限有关，详情见  Django 静态文件 和   Django 部署  

---

有时候有一些模板不是属于app的，比如 `baidutongji.html`, `share.html`等，  

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates').replace('\\', '/'),
            os.path.join(BASE_DIR,'templates2').replace('\\', '/'),
        ],
        'APP_DIRS': True,
]
```

这样 就可以把模板文件放在 templates 和 templates2 文件夹中了。  
