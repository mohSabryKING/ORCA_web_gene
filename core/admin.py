from django.contrib import admin
from .models import *
# Register your models here.
from django.contrib.admin import AdminSite



class Admin_1(admin.ModelAdmin):pass
class Admin_2(admin.ModelAdmin):pass
class Admin_3(admin.ModelAdmin):pass
class Admin_4(admin.ModelAdmin):pass
class Admin_5(admin.ModelAdmin):pass
    

admin.site.login_template='registration/login.html'
admin.site.logout_template='registration/logout.html'

admin.site.register(Client_country,Admin_1)
admin.site.register(Service_offers,Admin_2)
admin.site.register(Employee_model,Admin_3)
admin.site.register(Client_requests,Admin_4)
admin.site.register(Projects,Admin_5)

 