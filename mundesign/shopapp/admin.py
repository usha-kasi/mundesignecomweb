from django.contrib import admin
from .models import Address, PaymentDetails, Order, Wishlist, Recommendation, OrderItem

# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'line1', 'line2', 'city', 'state', 'postal_code', 'country')

class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'card_number', 'expiry_date', 'cvv')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'tracking_number')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product_name', 'quantity')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'item_name')

class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('user', 'recommended_item')

admin.site.register(Address, AddressAdmin)
admin.site.register(PaymentDetails, PaymentDetailsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Recommendation, RecommendationAdmin)
