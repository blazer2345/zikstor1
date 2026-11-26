from django.contrib import admin

# Register your models here.
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'product_name',
        'seller_name',
        'price',
        'whatsapp_number',
        'status',
        'date_uploaded',
    )

    list_filter = (
        'status',
        'date_uploaded',
    )

    search_fields = (
        'product_name',
        'seller_name',
        'whatsapp_number',
    )

    list_editable = ('status',)

    readonly_fields = ('date_uploaded',)

    actions = ['approve_products', 'reject_products']

    @admin.action(description='Approve selected products')
    def approve_products(self, request, queryset):
        queryset.update(status='approved')

    @admin.action(description='Reject selected products')
    def reject_products(self, request, queryset):
        queryset.update(status='rejected')