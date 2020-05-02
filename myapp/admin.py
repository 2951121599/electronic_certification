from django.contrib import admin
from .models import User, Yyzz

# Register your models here.
admin.site.site_header = "电子证照管理系统"
admin.site.site_title = "后台管理界面"

admin.site.register(User)
admin.site.register(Yyzz)
