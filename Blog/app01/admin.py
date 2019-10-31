from django.contrib import admin

# Register your models here.
from .models import Shop,Menu,Custom,Type,Order,Orderdetail,Orderitem

admin.site.register(Shop)
admin.site.register(Menu)
admin.site.register(Custom)
admin.site.register(Type)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Orderitem)