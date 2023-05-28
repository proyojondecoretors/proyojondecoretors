from django.contrib import admin
from .models import Product,ActiveOrder
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'total_amount', 'available', 'on_order']
admin.site.register(Product, AuthorAdmin)
admin.site.register(ActiveOrder)
