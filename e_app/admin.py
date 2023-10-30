from django.contrib import admin

from e_app.models import Cart, CartItem, Catagories, Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price']
admin.site.register(CartItem)
admin.site.register(Cart)
# admin.site.register
@admin.register(Catagories)
class CataforiesAdmin(admin.ModelAdmin):
    list_display=['id','name']
