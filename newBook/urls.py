"""newBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from learn import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'',views.index),
    # 调取views.py页面函数返回的页面路径
    url(r'^your$',views.hello)  #http://127.0.0.1:8001/your   '^'匹配路径开始+匹配路径名字字符等+'$'匹配路径结束
]
