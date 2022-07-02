from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True) #创建主键
    username = models.CharField(max_length=32) #用户名
    password = models.CharField(max_length=32) #密码