from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """ 用户学习的主题 """
    # 文本
    text = models.CharField(max_length=200)
    # 日期与时间，自动添加
    date_added = models.DateTimeField(auto_now_add=True)
    # 绑定用户
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Detail(models.Model):
    """ 主题内内容 """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # 模型复数
    class Meta:
        verbose_name_plural = 'details'

    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:50]}...'
        else:
            return self.text


