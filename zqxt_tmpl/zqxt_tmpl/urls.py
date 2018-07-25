"""zqxt_tmpl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from learn import views as learn_views          # 导入learn应用中的views文件，为防止文件名冲突使用as重命名

urlpatterns = [
    url(r'^$', learn_views.home_text, name='home_text'),        # 添加learn.home_text()函数
    url(r'^for/', learn_views.home_for, name='home_for'),       # 添加learn.home_for()函数
    url(r'^dict/', learn_views.home_dict, name='home_dict'),    # 添加learn.home_dict()函数
    url(r'^list/', learn_views.home_list, name='home_list'),    # 添加learn.home_list()函数
    url(r'^admin/', admin.site.urls),
]
