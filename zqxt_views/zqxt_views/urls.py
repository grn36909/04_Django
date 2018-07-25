"""zqxt_views URL Configuration

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
from calc import views as calc_views                # 导入calc应用中的views文件，为防止文件名冲突使用as重命名

urlpatterns = [
    url(r'^$', calc_views.index, name='home'),      # 添加index()函数, 对应URL为/index.html
    url(r'^add/$', calc_views.add, name='add'),     # 添加calc_views中的add()函数, 对应URL为^add/$
  # url(r'^add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),   # (\d+) = 一个或多个数字
    url(r'^add/(\d+)/(\d+)/$', calc_views.old_add2_redirect),   # 转换url, 并重定向
    url(r'^new_add/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
]