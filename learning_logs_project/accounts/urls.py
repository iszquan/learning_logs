# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2024/6/29 17:34
# @Author : ZQ
# @File : urls
# @Project : learning_logs_project
# @FileSummarize ： 
# --------    -------    --------
from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
    # django默认的身份验证url
    path('', include('django.contrib.auth.urls')),
    # 注册页面
    path('register/', views.register, name='register')
]