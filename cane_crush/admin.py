# admin.py
from django.contrib import admin
from .models import Category, Product, Customer, Order, OrderItem, PackSize


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



class PackSizeInline(admin.TabularInline):
    model = Product.pack_size.through
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'original_price', 'stock', 'available')
    list_filter = ('category', 'available')
    search_fields = ('name', 'category__name')
    exclude = ('slug',)
    inlines = [PackSizeInline]
    filter_horizontal = ('pack_size',)

@admin.register(PackSize)
class PackSizeAdmin(admin.ModelAdmin):
    list_display = ('size',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created', 'updated', 'paid')
    list_filter = ('created', 'updated', 'paid')
    search_fields = ('id', 'customer__user__username')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'timestamp')