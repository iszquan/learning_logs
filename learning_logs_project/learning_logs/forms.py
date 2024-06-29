# --------    -------    --------
# -*- coding: utf-8 -*-
# @Time : 2024/6/28 16:30
# @Author : ZQ
# @File : forms
# @Project : learning_logs_project
# @FileSummarize ： 
# --------    -------    --------
from django import forms
from .models import Topic, Detail

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 100})}