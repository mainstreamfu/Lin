"""s1_cnblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path,include
from app01 import views
from django.views.static import serve#导入静态文件处理的views控制包
from s1_cnblog import settings#导入项目文件夹中settings中的MEDIA_ROOT绝对路径

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/',views.log_in),
    path('logout/',views.log_out),
    path('index/',views.index),
    path('register/',views.register),
    path('get_valid_img/',views.get_valid_img),
    #app01 url 的分发
    path('app01/',include('app01.urls')),
    #media的配置
    re_path('media/(?P<path>.*)',serve,{'document_root':settings.MEDIA_ROOT}),
    #配置关于文章添加添加中的文件上传路径，文本编辑器的指定路径
    path('upload_file/',views.upload_file),
]
