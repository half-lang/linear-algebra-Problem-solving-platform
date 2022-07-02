from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)  #创建主键
    username = models.CharField(max_length=32) #账户
    password = models.CharField(max_length=32) #密码
    email = models.CharField(max_length=32,default="2020@qq.com")#邮箱
    telephone = models.CharField(max_length=32,default='00001')
    sex = models.CharField(max_length=20,default="male")#性别
    age = models.IntegerField(default=2)#年龄
    def __unicode__(self):
        return self.username