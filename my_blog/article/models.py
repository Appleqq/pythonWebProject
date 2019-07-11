from django.db import models

# Create your models here.

# 导入内建的User 模型
from django.contrib.auth.models import User

# timezone 处理时间相关事务
from  django.utils import timezone

class ArticlePost(models.Model):
    # 文章作者 参数 on_delete 用于指定删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题
    title = models.CharField(max_length=100)

    # 文章正文  保存大量文本使用 TextField
    body = models.TextField()

    # 文章创建时间 参数 default=timezone.now 指定其在创建数据时将默认写入到当前时间
    created = models.DateTimeField(default=timezone.now)

    # 文章更新时间 参数 auto_now=True 指定每次数据更新时候自动写入当前时间
    update = models.DateTimeField(auto_now=True)

    class Meta:

        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)


    def __str__(self):

        # return self.title 将文章标题返回
        return self.title