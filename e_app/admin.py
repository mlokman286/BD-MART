from django.contrib import admin

from e_app.models import MenProduct

# Register your models here.
@admin.register(MenProduct)
class MenProductAdmin(admin.ModelAdmin):
    list_display=['title','price']
