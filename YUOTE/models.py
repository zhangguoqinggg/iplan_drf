from django.db import models
# 建立一个python manage.py createsuperuser  user:zgq pwd : 1234
# Create your models here.
class MCompany(models.Model):
    company_name = models.CharField(max_length=20)
    #返回admin管理页面 对应到元素的名称
    def __str__(self):
        return self.company_name


class MCustomer(models.Model):
    customer_name = models.CharField(max_length=100)
    industy_type = models.IntegerField(verbose_name="客户类型",choices=((1,'汽车'),(2,'快消')))
    # 返回admin管理页面 对应到元素的名称
    def __str__(self):
        return self.customer_name


