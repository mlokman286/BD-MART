from django.contrib import admin

from e_app.models import Cart, CartItem, Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['title','price']
admin.site.register(CartItem)
admin.site.register(Cart)
