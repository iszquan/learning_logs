# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2024/6/27 20:26
# @Author : ZQ
# @File : urls
# @Project : learning_logs_project
# @FileSummarize ： 定义learning_logs的url模式
# --------    -------    --------
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    # 基础路由，调用方法，      /index
    path('', views.index, name='index'),
    # 显示所有主题的网页
    path('topics/', views.topics, name='topics'),
    # 详情页
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 新增topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # 新建详情
    path('new_detail/<int:topic_id>/', views.new_detail, name='new_detail'),
    # 编辑详情
    path('edit_detail/<int:detail_id>/', views.edit_detail, name='edit_detail')
]