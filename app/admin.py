from django.contrib import admin
from app.models import Customer, Product, OrderPlaced, User, Cart
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ["id","user","name","locality","city","zipcode","state",]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["title","selling_price","discount_price","description","brand","category","product_image",]


class CartAdmin(admin.ModelAdmin):
    list_display = [
        "user","product","quantity", ]


class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = [ "user", "customer","product","quantity","order_date","status",]



admin.site.register(Customer,CustomerAdmin )
admin.site.register(Product,ProductAdmin )
admin.site.register(Cart,CartAdmin )
admin.site.register(OrderPlaced, OrderPlacedAdmin ) 