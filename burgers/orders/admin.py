from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','fio','email','address','phone', 'pickup','created','payment_method', 'paid']
    list_filter = ['fio','email','address','phone','pickup','payment_method']
    inlines = [OrderItemInline]

admin.site.register(Order,OrderAdmin)