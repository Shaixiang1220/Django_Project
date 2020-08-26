from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=50)
    content = models.CharField('信息内容', max_length=200)
    timestamp = models.DateField('反馈时间', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '信息反馈表'
        verbose_name_plural = '信息反馈表'