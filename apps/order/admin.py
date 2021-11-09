from django.contrib import admin

from apps.order.models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'email', 'address', 'zipcode',
                    'place', 'phone', 'created_at',
                    'paid_amount')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product',
                    'vendor', 'vendor_paid',
                    'price', 'quantity')
