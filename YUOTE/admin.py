from django.contrib import admin
from .models import MCompany,MCustomer
#注册公司信息表
admin.site.register(MCompany)
# Register your models here.
admin.site.register(MCustomer)