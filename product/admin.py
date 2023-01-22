from django.contrib import admin
from product.models import Weight, Product 
# Register your models here.

@admin.register(Weight)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("weight_range", "price", )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "fullname", )




