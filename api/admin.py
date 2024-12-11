from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# Registering the models
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

# from django.contrib import admin
# from .models import Category, Product, Order, OrderItem

# # Registering the models with customization
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description')  # Columns to display in the list view
#     search_fields = ('name',)  # Allow searching by name

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'stock', 'category')  # Columns to display
#     search_fields = ('name', 'category__name')  # Search by product name and category
#     list_filter = ('category',)  # Filter by category

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ('customer_name', 'customer_email', 'created_at')  # Columns to display
#     search_fields = ('customer_name', 'customer_email')  # Search by name or email
#     ordering = ('-created_at',)  # Order by creation date (newest first)

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product', 'quantity')  # Columns to display
